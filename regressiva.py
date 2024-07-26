def regressiva(X):
    print(X)
    regressiva(X-1)
    
    
    def regressiva(X):
        if X <=0:
            print("Acabou")
        else:
            print(X)
            regressiva(X-1)
                