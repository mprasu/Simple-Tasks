
class question:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
        
Questions=[
    "List is a mutable object or immutable object?\n(a)Immutable\n(b)Mutable\n(c)Both\n\n",
    "Square root of 625 is?\n(a)15\n(b)35\n(c)25\n\n",
    "Python supports___\n(a)both\n(b)OOPs\n(c)Inheritance\n\n",
    ]

question_answer=[
    question(Questions[0],"b"),
    question(Questions[1],"c"),
    question(Questions[2],"a"),
    ]

def checking_answer(question_answer):
    score=0
    for q in question_answer:
        answer=input(q.prompt)
        if answer==q.answer:
            score+=1
    print("You got"+str(score)+"/"+str(len(question_answer)) +"correct")
checking_answer(question_answer)

    
