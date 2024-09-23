from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey("Courses.Course", on_delete=models.CASCADE)
    createion_date = models.DateTimeField(auto_now_add=True)
    scheduled_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.title
    
class Question(models.Model):
    QUESTION_TYPE_CHOICES = [
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False'),]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.TextField()
    question_type = models.CharField(max_length=15,choices=QUESTION_TYPE_CHOICES)
    correct_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return f"{self.student.username} - {self.question.text}"
    
    def is_correct(self):
        # Compare student's answer with the correct answer stored in the Question model
        return self.text.strip().lower() == self.question.correct_answer.strip().lower()

class Result(models.Model):
    student = models.ForeignKey('Accounts.CustomUser', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    completion_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
       
    def __str__(self):
        return f"{self.student.username} - {self.quiz.title} (Score: {self.score})"
    
    @classmethod
    def calculate_score(cls, student, quiz):
        answers = Answer.objects.filter(student=student, question__quiz=quiz)
        correct_answers_count = sum(1 for answer in answers if answer.is_correct())
        total_questions = quiz.question_set.count()
        
        # Calculate score as a percentage
        score = (correct_answers_count / total_questions) * 100 if total_questions > 0 else 0
        
        return cls.objects.create(student=student, quiz=quiz, score=score)