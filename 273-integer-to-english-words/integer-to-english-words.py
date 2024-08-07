class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        f19 = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        tens = {20: 'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty', 90:'Ninety'}
        hund = {0:'Hundred', 1:'Thousand', 2:'Million', 3:'Billion'}
        hundNum = [10**2, 10**3, 10**6, 10**9]

        
        ans = ""
        n = len(str(num))
        place = n-1
        i = 0
        while i != -1:
            i = place//3
            sub = 0
            if i > 0:
                temp = num//hundNum[i]
            else:
                i = -1
                temp = num % 1000
            if temp == 0:
                place -= 1
                continue

            if temp >= 100:
                ans += f19[temp//100] + " "
                ans += "Hundred "
                temp = temp % 100
                sub = max(sub, 3)
            
            if temp >= 20:
                ans += tens[(temp//10)*10] + " "
                temp = temp % 10
                sub = max(sub, 2)
            
            if temp < 20 and temp >= 1:
                ans += f19[temp] + " "
                if temp > 9:
                    sub = max(sub, 2)
                else:
                    sub = max(sub, 1)

            if i > 0:
                ans += hund[i] + " "
                num = num % hundNum[i]
            place = place - sub

        return ans.rstrip()

            