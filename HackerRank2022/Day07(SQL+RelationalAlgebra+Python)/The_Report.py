# You are given two tables: Students and Grades.
# Students contains three columns ID, Name and Marks.
#
# Grades contains the following data:
#
# Ketty gives Eve a task to generate a report containing
# three columns: Name, Grade and Mark. Ketty doesn't want
# the NAMES of those students who received a grade lower
# than 8. The report must be in descending order by grade
# -- i.e. higher grades are entered first. If there is
# more than one student with the same grade (8-10)
# assigned to them, order those particular students by
# their name alphabetically. Finally, if the grade is
# lower than 8, use "NULL" as their name and list them
# by their grades in descending order. If there is more
# than one student with the same grade (1-7) assigned
# to them, order those particular students by their
# marks in ascending order.
#
# Write a query to help Eve.
#
# Note
#
# Print "NULL"  as the name if the grade is less than 8.

SELECT IF(GRADE >7, NAME, NULL), GRADE, MARKS FROM STUDENTS
JOIN GRADES WHERE MARKS BETWEEN MIN_MARK AND MAX_MARK
ORDER BY GRADE DESC, NAME


ONLINE SOLUTION:
SELECT
  CASE
    WHEN GRADES.GRADE >= 8 THEN STUDENTS.NAME
    WHEN GRADES.GRADE < 8 THEN 'NULL'
  END AS NAME,
  GRADES.GRADE,
  STUDENTS.MARKS
FROM STUDENTS
  LEFT JOIN GRADES ON STUDENTS.MARKS >= MIN_MARK
  AND STUDENTS.MARKS <= MAX_MARK
ORDER BY
  GRADES.GRADE DESC, STUDENTS.NAME ASC, STUDENTS.MARKS ASC;