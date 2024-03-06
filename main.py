#Function: This program determines if a student will be admitted or rejected.

#Input:  Interactive

#Output: Accept or Reject

# Get input and covert to correct data type for testScore and classRank

# Test using admission requirement and print Accept or Reject

testScoreString = input("Enter the student's test score: ")
classRankString = input("Enter the studnet's class rank: ")

testScore = int(testScoreString)
classRank = int(classRankString)

if testScore >= 90:
  if classRank >= 25:
    print("Accept")
  else:
    print("Reject")
else:
  if testScore >= 80:
    if classRank >= 50:
      print("Accept")
    else:
      print("Reject")
  else:
    if testScore >= 70:
      if classRank >= 75:
        print("Accept")
      else:
        print("Reject")
    else:
      print("Reject")