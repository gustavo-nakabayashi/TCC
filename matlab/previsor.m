close all;
clear all;
clc;

% leitura da base da dados xt, ydt, xv, ydv


load  bolsa2.csv

x1=bolsa2;

np=length(x1);

x2=atraso2(1,x1);
x3=atraso2(2,x1);
x4=atraso2(3,x1);
x4=atraso2(4,x1);
x5=atraso2(5,x1);
x6=atraso2(6,x1);
x7=atraso2(7,x1);

ndp=1;
x = [x1(1:np-ndp) x2(1:np-ndp) x3(1:np-ndp) x4(1:np-ndp) x5(1:np-ndp) x6(1:np-ndp) x7(1:np-ndp)];

yd=avanco2(ndp,x1);

np=length(yd);

npt=1000;

xt=x(8:npt,:);
ydt=yd(8:npt);
npt=npt-8;

npv=np-npt;

xv=x(npt+1:np,:);
ydv=yd(npt+1:np);

n=length(xv(1,:));
m=5;
alfa=0.1;
nepocas=5;

xmin=min(xt);

xmax=max(xt);

delta=(xmax-xmin)/(m-1);

for j=1:m
    for i=1:n
        b(i,j)=xmin(i)+(j-1)*delta(i);
    end
end

w=zeros(n,m);

%treinanemento off line

for epoca=1:nepocas
    for k=1:npt
        % calcular a saida para a entrada xt(k,:)
        [ysk k1 k2 mik1 mik2 yi]= cal2yamaka(xt(k,:),n,m,1,delta,b,xmin,xmax,w);

        for i=1:n
            w(i,k1(i))=w(i,k1(i)) - alfa*(ysk-ydt(k))*mik1(i);
            w(i,k2(i))=w(i,k2(i)) - alfa*(ysk-ydt(k))*mik2(i);
        end

    end

end


ys=[];
ajuste=0;

for k=1:npv

    % calcular a saida para a entrada xt(k,:)
    [ysk k1 k2 mik1 mik2 yi] = cal2yamaka(xv(k,:),n,m,1,delta,b,xmin,xmax,w);


    ys(k)=ysk;

   
    alfa=0;

    for i=1:n
        alfa=alfa+(mik1(i)^2 + mik2(i)^2);
    end
    alfa=1/alfa;

    if  mod(k,1) == 0
        for i=1:n
            w(i,k1(i))=w(i,k1(i)) - alfa*(ysk-ydv(k))*mik1(i);
            w(i,k2(i))=w(i,k2(i)) - alfa*(ysk-ydv(k))*mik2(i);
        end;
    end

    % Adaptação de contexto, ajuste xmin e xmax

    if ysk<xmin(1)
        xmin(:)=ysk;
        ajuste=1;
    end
    if ysk>xmax(1)
        xmax(:)=ysk;
        ajuste=1;
    end

    if ajuste==1
        delta=(xmax-xmin)/(m-1);
        for j=1:m
            for i=1:n
                b(i,j)=xmin(i)+(j-1)*delta(i);
            end
        end

  
    end
    ajuste=0;

end

acerto=0;

for k=2:npv
    aux=(ys(k)-ys(k-1))*(ydv(k)-ydv(k-1));
    if aux>=0
        acerto=acerto+1;
    end
   
end

acerto_percentual = acerto*100/npv


figure
plot(ys);
hold on
plot(ydv,'k')

for k=1:npv
    erro2(k)=100*abs((ydv(k)-ys(k))/ydv(k));

end

% figure
% hist(erro2,20)

epm=sum(erro2)/npv

a=corrcoef(ydv,ys);
R2=a(1,2)