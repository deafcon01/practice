def towerofHanoi(n, fromrod, torod, auxrod):
    if n==0:
        return
    towerofHanoi(n-1, fromrod, auxrod,torod)
    print(f"Move disk {n} from rod {fromrod} to rod {torod}")
    towerofHanoi(n-1, auxrod, torod,fromrod)

if __name__=="__main__":
    n=3
    towerofHanoi(n, 'A', 'C', 'B')