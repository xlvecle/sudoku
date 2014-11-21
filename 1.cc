#include <cstdio>
#include <cstring>
const int N=9;
const int maxr = N*N*N+10;
const int maxc = N*N*4+10;
const int maxn = maxr*4+maxc+10;
char *g;
struct DLX
{
    int n,m,size;
    int U[maxn],D[maxn],R[maxn],L[maxn],Row[maxn],Col[maxn];
    int H[maxr],S[maxc];
    int ansd,ans[maxr];
    void init(int _n,int _m)
    {
        n = _n;
        m = _m;
        for(int i = 0;i <= m;i++)
        {
            S[i] = 0;
            U[i] = D[i] = i;
            L[i] = i-1;
            R[i] = i+1;
        }
        R[m] = 0; L[0] = m;
        size = m;
        for(int i = 1;i <= n;i++)H[i] = -1;
    }
    void Link(int r,int c)
    {
        size++;
        S[c]++;
        Col[size]=c;
        Row[size] = r;
        D[size] = D[c];
        U[D[c]] = size;
        U[size] = c;
        D[c] = size;
        if(H[r] < 0)H[r] = L[size] = R[size] = size;
        else
        {
            R[size] = R[H[r]];
            L[R[H[r]]] = size;
            L[size] = H[r];
            R[H[r]] = size;
        }
    }
    void remove(int c)
    {
        L[R[c]] = L[c]; R[L[c]] = R[c];
        for(int i = D[c];i != c;i = D[i])
            for(int j = R[i];j != i;j = R[j])
            {
                U[D[j]] = U[j];
                D[U[j]] = D[j];
                --S[Col[j]];
            }
    }
    void restore(int c)
    {
        for(int i = U[c];i != c;i = U[i])
            for(int j = L[i];j != i;j = L[j])
                ++S[Col[U[D[j]]=D[U[j]]=j]];
        L[R[c]] = R[L[c]] = c;
    }
    bool Dance(int d)
    {
        if(R[0] == 0)
        {
            for(int i = 0;i < d;i++)g[(ans[i]-1)/9] = (ans[i]-1)%9 + '1';
            for(int i = 0;i < N*N;i++)printf("%c",g[i]);
            printf("\n");
            return true;
        }
        int c = R[0];
        for(int i = R[0];i != 0;i = R[i])
            if(S[i] < S[c])
                c = i;
        remove(c);
        for(int i = D[c];i != c;i = D[i])
        {
            ans[d] = Row[i];
            for(int j = R[i];j != i;j = R[j])
                remove(Col[j]);
            if(Dance(d+1))
                return true;
            for(int j = L[i];j != i;j = L[j])
                restore(Col[j]);
        }
        restore(c);
        return false;
    }
};
void place(int &r,int &c1,int &c2,int &c3,int &c4,int i,int j,int k)
{
    r = (i*N+j)*N+k;
    c1 = i*N+j+1; 
    c2 = N*N+i*N+k;
    c3 = N*N*2+j*N+k; 
    c4 = N*N*3+((i/3)*3+(j/3))*N+k;
}
DLX dlx;
int main(int argc, char *argv[])
{
    g=argv[1];
    dlx.init(N*N*N,N*N*4);
    int r,c1,c2,c3,c4;
    for(int i = 0;i < N;i++)
        for(int j = 0;j < N;j++)
            for(int k = 1;k <= N;k++)
                if(g[i*N+j] == '.' || g[i*N+j] == '0'+k)
                {
                    place(r,c1,c2,c3,c4,i,j,k);
                    dlx.Link(r,c1);
                    dlx.Link(r,c2);
                    dlx.Link(r,c3);
                    dlx.Link(r,c4);
                }
    if(dlx.Dance(0)==0)
    {
        for(int i=0;i<81;i++)
            printf("0");
        printf("\n");
    }
    return 0;
}