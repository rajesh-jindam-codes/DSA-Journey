class Solution:
    def studentAttendanceRecord(self,s):
        lateStreak=0
        absent=0
        for ch in s:
            if ch =='A':
                absent+=1
                if absent>=2:
                    return False
                lateStreak=0
            elif ch =='L':
                lateStreak+=1
                if lateStreak>=3:
                    return False
            else:
                lateStreak=0
        return True
obj=Solution()
print(obj.studentAttendanceRecord('PAPPPLLL'))