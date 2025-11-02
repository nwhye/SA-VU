using System;
using System.Collections.Generic;

class Student
{
    public string? Name { get; set; }
    public int Age { get; set; }
}

class Program
{
    static void Main()
    {
        List<Student> students = new List<Student>
        {
            new Student { Name = "Daniil", Age = 17 },
            new Student { Name = "Hanna", Age = 20 },
            new Student { Name = "Artem", Age = 18 },
            new Student { Name = "Anna", Age = 19 },
            new Student { Name = "Ivan", Age = 18 }
        };

        Student youngestStudent = students[0];

        foreach (Student student in students)
        {
            if (student.Age < youngestStudent.Age)
            {
                youngestStudent = student;
            }
        }
        Console.WriteLine("The youngest student is " + youngestStudent.Name);
    }
}
