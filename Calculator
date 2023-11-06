#include <iostream.h>
#include <conio.h>
void main(){
clrscr();
int a,b,result;
int ch;
cout<<“Enter two numbers:”;
cin>>a>>b;
cout<<“1.Add /n 2.Sub /n 3.Mul /n 4.Div”<<endl;
cin>>ch;
switch(ch){
case 1:{
asm mov ax,a;
asm mov bx,b;
asm add ax,bx;
asm mov result,ax;
cout<<“Result:”<<result;
break;
}
case 2:{
asm mov ax,a;
asm mov bx,b;
asm sub ax,bx;
asm mov result,ax;
cout<<“Result:”<<result;
break;
}
case 3:{
asm mov ax,a;
asm mov bx,b;
asm mul bx;
asm mov result,ax;
cout<<“Result:”<<result;
break;
}
case 4:{
asm mov ax,a;
asm mov bx,b;
asm div bx;
asm mov result,ax;
cout<<“Result:”<<result;
break;
}
}
getch();
}
