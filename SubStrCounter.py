# https://stepik.org/lesson/24469/step/7?unit=6775


s,t = (input() for _ in range(2))

def f(s,t,counter=0):
    for i in range(len(s)):
        if s.find(t,i,i+len(t)) >=0:
            counter+=1
    return counter



if __name__ == '__main__':
    print(f(s,t))