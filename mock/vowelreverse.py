def reverseVowels(s: str) -> str:
        a=s.split()
        vowels=['a','e','i','o','u']
        l,r=0,len(s)-1
        while l<=r:
            if a[l] in vowels:
                if a[r] not in vowels:
                    r-=1
                else:
                    a[l],a[r]=a[r],a[l]
            else:
                l+=1
            if a[r] in vowels:
                if a[l] not in vowels:
                    l+=1
                else:
                    a[l],a[r]=a[r],a[l]
            else:
                r-=1
        return "".join(a)

if __name__ == '__main__':
    s="hello"
    print(reverseVowels(s))