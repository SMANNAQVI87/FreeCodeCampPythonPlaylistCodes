from enum import Enum 
print(3<<2) #12
print(3>>2) #0
class Courses_of_this_semester(Enum):
    Bio_Robotics = "Shamim Sir,slides analysis"
    Computational_Human_Robot_Interaction = "Abhishek Sir, Previous Year 4-1 and Slides"
    Computer_Vision = "Mehedi Sir,Practice Coding of Machine Learning and Convolutional Neural Networks"
    IoT = "Lafifa madam, Practice Comprehensive Videos from NptelHRD"

print(Courses_of_this_semester['Bio_Robotics'].value)
Course1 = Courses_of_this_semester.Bio_Robotics.value.lower() 
Course2 = Courses_of_this_semester.Computational_Human_Robot_Interaction.value.lower()
Course3 = Courses_of_this_semester.Computer_Vision.value.lower()
Course4 = Courses_of_this_semester.IoT.value.lower()

list_of_courses = [Course1,
                   Course2,
                   Course3,
                   Course4]
Answer = sorted(list_of_courses,reverse=True,key=str.upper)
print(Answer)
