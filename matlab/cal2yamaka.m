function [ys, k1, k2, mik1, mik2, y] = cal2yamaka(x,n,m,np,delta,b,xmin,xmax,w)

for k=1:np
    for i=1:n
        
        if x(k,i)<=xmin(i)
            k1(i)=1;
            mik1(i)=1;
        else if x(k,i)>=xmax(i)
                k1(i)=m-1;
                mik1(i)=0;
            else
                
                k1(i)=fix((x(k,i)-xmin(i))/delta(i)) + 1;
                mik1(i)=-(x(k,i) - b(i,k1(i)))/delta(i)+1;
                
            end
        end
        
        k2(i)=k1(i)+1;
        mik2(i)=1 - mik1(i);
        y(i)=mik1(i)*w(i,k1(i)) + mik2(i)*w(i,k2(i));
    end
    ys(k)=sum(y);
end
end