

int fib(int n){
    int *dp=(int*)malloc((n+1)*sizeof(int));
    int i;
    for(i-0;i<=n;i++) dp[i]=-1;
    if (n==0) return 0;
    dp[0]=0;
    dp[1]=1;
    for( i=2;i<=n;i++)
    {
        dp[i]=dp[i-1]+dp[i-2];
    }
    return dp[n];
}