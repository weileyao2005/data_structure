6-2
分数 17
哈夫曼编码
作者 魏峻
单位 陕西理工大学
本题要求根据输入创建哈夫曼编码。

输入4 个字符以及该字符对应的权值(如:a,10)

输出每个节点的哈夫曼编码。 

输入样例为：

a,10
b,9
c,12
d,8
输出样例为：

a:10
b:00
c:11
d:01
#include<stdio.h>
    return 0;}

/* === 答案代码块 === */
void createHuffmanTree(HuffmanTree HT, int *w, int n){
    if(n<=1)
        return;
    for(int i=1; i<=n; i++){
        HT[i].weight=
w[i];
        HT[i].lchild=
0;
        HT[i].parent=
0;
        HT[i].rchild=
0; }
    for(int i=
n + 1; i<=M; i++){
        HT[i].weight=0;
        HT[i].lchild=0;
        HT[i].parent=0;
        HT[i].rchild=0; }
    for (int i=n+1; i<=M; i++){
        int s1,s2;
        select(HT,i-1,&s1,&s2);
        HT[s1].parent=i;
        HT[s2].parent=i;
        HT[i].lchild=
s1;
        HT[i].rchild=
s2;
        HT[i].weight=
HT[s1].weight + HT[s2].weight; }}

void select(HuffmanTree HT, int k, int *s1, int *s2){
    unsigned int tmp=MAX,tmpi=0;
    for (int i=1; i<=k; i++){
        if(!HT[i].parent){
            if(tmp>HT[i].weight){
                tmp=HT[i].weight;
                tmpi=i;}}}
    *s1=tmpi;
    tmp=MAX;
    tmpi=0;
    for(int i=1; i<=k; i++){
        if((!HT[i].parent)&&i!=*s1){
            if(tmp>HT[i].weight){
                tmp=HT[i].weight;
                tmpi=i;}}}
    if(tmpi<*s1){
        *s2=*s1;
        *s1=tmpi;}
    else
        *s2=tmpi;}

void encodingHuffmanCode(HuffmanTree HT, HuffmanCode HC){
    char tmp[N];
    tmp[N-1]=
'\0';
    int start,c,f;
    for (int i=1; i<=N; i++){
        start=N-1;
        for(c=i,f=
HT[i].parent; f!=0; c=f,f=
HT[f].parent){
            if(HT[f].lchild==c)
                tmp[--start]=
'0';
            else
                tmp[--start]=
'1'; }
        HC[i]=(char*)malloc((N-start)*sizeof(char));
        strcpy (HC[i],&tmp[start]);}}

void printHuffmanCoding(HuffmanCode HC, char ch[]){
    for(int i=1; i<=N; i++){
        printf("%c:%s\n",ch[i],HC[i]);}}

6-1
扩展的先序遍历序列创建二叉树
作者 DS课程组
单位 临沂大学
以扩展的先序遍历建立二叉树，根结点的地址通过函数值返回。

例如 

输入AB#DF##G##C##,建立二叉树如下图，

二叉树.png

输出该二叉树的先序遍历序列ABDFGC。

#include <stdio.h>
#include <stdlib.h>

typedef char ElementType;
typedef struct BiTNode{
    ElementType data;
    struct BiTNode *lchild;
    struct BiTNode *rchild;
}BiTNode,*BiTree;

BiTree CreatBinTree();
void  preorder( BiTree T );

int main()
{
    BiTree T = CreatBinTree();
    preorder(  T );
    return 0;
}
void  preorder( BiTree T )
{
   if(T)
   {
     printf("%c",T->data);
     preorder(T->lchild);
     preorder(T->rchild);
   }
}
/* === 答案代码块 === */
BiTree CreatBinTree()
{
   char ch;BiTree T;
   scanf("%c",&ch);
   if(ch=='#') return 
NULL;
   T=
(BiTree)malloc(sizeof(BiTNode));
   T->data=ch;
   T->lchild=
CreatBinTree();
   T->rchild=
CreatBinTree();
   return T;
}
评测结果
答案正确
得分
8 分
分数 6
计算二叉树的深度
作者 余雨萍
单位 中原工学院
使用递归方式计算二叉树的深度。提示：二叉树是根据先序遍历顺序建立起来的。

#include<stdio.h>
#include<stdlib.h>
typedef struct BiNode
{
    char data;
    struct BiNode *lchild, *rchild;
}BiTNode, *BiTree;

void CreateBiTree(BiTree * T)
{
    char ch;
    scanf("%c", &ch);
    if (ch == '#')
        *T = NULL;
    else
    {
        *T = (BiTree)malloc(sizeof(BiTNode));
        (*T)->data = ch;
        CreateBiTree(&(*T)->lchild);
        CreateBiTree(&(*T)->rchild);
    }
}

/* === 答案代码块 === */
int Depth(BiTree T)
{
    int m, n;
    if (
T == NULL)
        return 0;
    else
    {
        m = 
Depth(T->lchild);
        n = 
Depth(T->rchild);
        if (m > n)
            return(m + 1);
        else
            return (n + 1);
    }
}

int main()
{
    BiTree tree = NULL;
    CreateBiTree(&tree);
    int depth = Depth(tree);
    printf("%d", depth);
    return 0;
}
测试数据

ab##c##.png

输入：ab##c## 

输出：2

评测结果
答案正确
得分
6 分
分数 6
先序+中序创建二叉树
作者 DS课程组
单位 临沂大学
已知先序遍历序列和中序遍历序列建立二叉树。
例如 

二叉树.png

输入先序遍历序列：
ABDFGC，
再输入中序遍历序列：
BFDGAC，则
输出该二叉树的后序遍历序列：
FGDBCA。

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef char ElementType;
typedef struct BiTNode{
    ElementType data;
    struct BiTNode *lchild;
    struct BiTNode *rchild;
}BiTNode,*BiTree;

BiTree CreatBinTree(char *pre,char *in,int n );
void postorder( BiTree T );

int main()
{
    BiTree T;
    char prelist[100];
    char inlist[100];
    int length;
    scanf("%s",prelist);
    scanf("%s",inlist);
    length=strlen(prelist);
    T=CreatBinTree(prelist,inlist, length);
    postorder(  T );
    return 0;
}
void  postorder( BiTree T )
{
    if(T)
    {
        
        postorder(T->lchild);
        postorder(T->rchild);
        printf("%c",T->data);
    }
}
/* === 答案代码块 === */
BiTree CreatBinTree(char *pre,char *in,int n)
{
    BiTree T;
    int i;
    if(n<=0) return NULL;
    T=(BiTree)malloc(sizeof(BiTNode));
    T->data=pre[0];
    for(i=0;in[i]!=pre[0];i++);
    T->lchild=
CreatBinTree(pre + 1, in, i);
    T->rchild=
CreatBinTree(pre + i + 1, in + i + 1, n - i - 1);
    return T;
}
评测结果
答案正确
得分
6 分

6-1 先序输出叶结点
分数 10
作者 陈越
单位 浙江大学
本题要求按照先序遍历的顺序输出给定二叉树的叶结点。

函数接口定义：
void PreorderPrintLeaves( BinTree BT );
其中BinTree结构定义如下：
typedef struct TNode *Position;
typedef Position BinTree;
struct TNode{
    ElementType Data;
    BinTree Left;
    BinTree Right;
};
函数PreorderPrintLeaves应按照先序遍历的顺序输出给定二叉树BT的叶结点，格式为一个空格跟着一个字符。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef char ElementType;
typedef struct TNode *Position;
typedef Position BinTree;
struct TNode{
    ElementType Data;
    BinTree Left;
    BinTree Right;
};

BinTree CreatBinTree(); /* 实现细节忽略 */
void PreorderPrintLeaves( BinTree BT );

int main()
{
    BinTree BT = CreatBinTree();
    printf("Leaf nodes are:");
    PreorderPrintLeaves(BT);
    printf("\n");

    return 0;
}
/* 你的代码将被嵌在这里 */
输出样例（对于图中给出的树）：

Leaf nodes are: D E H I
C (gcc)
/* === 答案代码块 === */
void PreorderPrintLeaves( BinTree BT )
{
    if (BT == NULL) return;                  // 空树直接返回
    
    // 先序遍历核心：先访问根结点
    if (BT->Left == NULL && BT->Right == NULL)  // 判断是否为叶结点
    {
        printf(" %c", BT->Data);              // 格式：一个空格 + 字符
    }
    
    PreorderPrintLeaves(BT->Left);           // 递归遍历左子树
    PreorderPrintLeaves(BT->Right);          // 递归遍历右子树
}

6-2 统计二叉树结点个数
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，可统计二叉树的结点个数。

函数接口定义：

int NodeCount ( BiTree T);
T是二叉树树根指针，函数NodeCount返回二叉树中结点个数，若树为空，返回0。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;
typedef struct BiTNode
{
    ElemType data;
    struct BiTNode *lchild,*rchild;
}BiTNode,*BiTree;

BiTree Create();/* 细节在此不表 */

int NodeCount ( BiTree T);

int main()
{
    BiTree T = Create();
    
    printf("%d\n", NodeCount(T));
    return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
输入为由字母和'#'组成的字符串，代表二叉树的扩展先序序列。例如对于如下二叉树，输入数据：

AB#DF##G##C##
输出样例（对于图中给出的树）：
二叉树.png

6
C (gcc)
/* === 答案代码块 === */
int NodeCount(BiTree T)
{
    if (T == NULL)
        return 0;
    return 1 + NodeCount(T->lchild) + NodeCount(T->rchild);
}
6-3 统计二叉树叶子结点个数
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，可统计二叉树的叶子结点个数。

函数接口定义：

int LeafCount ( BiTree T);
T是二叉树树根指针，函数LeafCount返回二叉树中叶子结点个数，若树为空，则返回0。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;
typedef struct BiTNode
{
    ElemType data;
    struct BiTNode *lchild,*rchild;
}BiTNode,*BiTree;

BiTree Create();/* 细节在此不表 */

int LeafCount ( BiTree T);

int main()
{
    BiTree T = Create();
    
    printf("%d\n", LeafCount(T));
    return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
输入为由字母和'#'组成的字符串，代表二叉树的扩展先序序列。例如对于如下二叉树，输入数据：

AB#DF##G##C##
输出样例（对于图中给出的树）：
二叉树.png

3
C (gcc)
/* === 答案代码块 === */
int LeafCount(BiTree T)
{
    if (T == NULL)
        return 0;
    if (T->lchild == NULL && T->rchild == NULL)
        return 1;
    return LeafCount(T->lchild) + LeafCount(T->rchild);
}
6-4 二叉树的层次遍历
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现给定的二叉树的层次遍历。

函数接口定义：

void Levelorder(BiTree T);

T是二叉树树根指针，Levelorder函数输出给定二叉树的层次遍历序列，格式为一个空格跟着一个字符。

其中BinTree结构定义如下：

typedef char ElemType;
typedef struct BiTNode
{
   ElemType data;
   struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;
裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;
typedef struct BiTNode
{
   ElemType data;
   struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;

BiTree Create();/* 细节在此不表 */

void Levelorder(BiTree T);

int main()
{
   BiTree T = Create();
   printf("Levelorder:"); Levelorder(T); printf("\n");
   return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
输入为由字母和'#'组成的字符串，代表二叉树的扩展先序序列。例如对于如下二叉树，输入数据：

AB#DF##G##C##
输出样例（对于图中给出的树）：
二叉树.png

Levelorder: A B C D F G

C (gcc)
/* === 答案代码块 === */
void Levelorder(BiTree T) {
    if (T == NULL) return;
    
    // 使用数组模拟队列，容量1000足以覆盖常规测试用例
    BiTree Q[1000]; 
    int front = 0, rear = 0;
    
    Q[rear++] = T; // 根结点入队
    while (front < rear) {
        BiTree p = Q[front++]; // 队头元素出队
        printf(" %c", p->data); // 题目要求：输出格式为一个空格跟着一个字符
        
        if (p->lchild != NULL) Q[rear++] = p->lchild; // 左孩子非空则入队
        if (p->rchild != NULL) Q[rear++] = p->rchild; // 右孩子非空则入队
    }
}
6-5 求二叉树的深度1
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，可返回二叉树的深度。

函数接口定义：

int Depth(BiTree T);
T是二叉树树根指针，函数Depth返回二叉树的深度，若树为空，返回0。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef char ElemType;
typedef struct BiTNode
{
    ElemType data;
    struct BiTNode *lchild, *rchild;
}BiTNode, *BiTree;

BiTree Create();/* 细节在此不表 */

int Depth(BiTree T);

int main()
{
    BiTree T = Create();

    printf("%d\n", Depth(T));
    return 0;
}
/* 你的代码将被嵌在这里 */
输入样例：
输入为由字母和'#'组成的字符串，代表二叉树的扩展先序序列。例如对于如下二叉树，输入数据：

AB#DF##G##C##
输出样例（对于图中给出的树）：
二叉树.png

4
C (gcc)
/* === 答案代码块 === */
int Depth(BiTree T)
{
    if (T == NULL)
        return 0;
    int left = Depth(T->lchild);
    int right = Depth(T->rchild);
    return (left > right ? left : right) + 1;
}
6-6 二叉树创建及遍历
分数 10
作者 王东
单位 贵州师范学院
实现二叉树创建及遍历算法。

函数接口定义：
void CreateBiTree(BiTree &T);//根据输入的字符串，创建二叉树。 
void PreOrder(BiTree T);//先序遍历二叉树 
void InOrder(BiTree T);//中序遍历二叉树 
void PostOrder(BiTree T);//后序遍历二叉树 
void LevelOrder(BiTree T);//层次遍历二叉树
其中 T 表示二叉树类型。

裁判测试程序样例：
#include<iostream>
using namespace std;
typedef struct BiNode{
    char data;
    struct BiNode *lchild,*rchild;
}BiTNode,*BiTree;

void CreateBiTree(BiTree &T);//根据输入的字符串，创建二叉树。 
void PreOrder(BiTree T);//先序遍历二叉树 
void InOrder(BiTree T);//中序遍历二叉树 
void PostOrder(BiTree T);//后序遍历二叉树 
void LevelOrder(BiTree T);//层次遍历二叉树  

int main(){
 BiTree T;
 CreateBiTree(T);
 cout<<"PreOrder:"; 
 PreOrder(T);
 cout<<endl<<"InOrder:";
 InOrder(T);
 cout<<endl<<"PostOrder:";
 PostOrder(T);
 cout<<endl<<"LevelOrder:";
 LevelOrder(T);
 return 0;
} 
/* 请在这里填写答案 */
输入样例：
ABD#E###CF##G##
输出样例：
PreOrder:ABDECFG
InOrder:DEBAFCG
PostOrder:EDBFGCA
LevelOrder:ABCDFGE
C++ (g++)
/* === 答案代码块 === */
// 根据扩展先序序列递归创建二叉树
void CreateBiTree(BiTree &T) {
    char ch;
    cin >> ch;
    if (ch == '#') {
        T = NULL;
    } else {
        T = new BiTNode;
        T->data = ch;
        CreateBiTree(T->lchild);   // 递归创建左子树
        CreateBiTree(T->rchild);   // 递归创建右子树
    }
}

// 先序遍历：根→左→右
void PreOrder(BiTree T) {
    if (T) {
        cout << T->data;
        PreOrder(T->lchild);
        PreOrder(T->rchild);
    }
}

// 中序遍历：左→根→右
void InOrder(BiTree T) {
    if (T) {
        InOrder(T->lchild);
        cout << T->data;
        InOrder(T->rchild);
    }
}

// 后序遍历：左→右→根
void PostOrder(BiTree T) {
    if (T) {
        PostOrder(T->lchild);
        PostOrder(T->rchild);
        cout << T->data;
    }
}

// 层次遍历
void LevelOrder(BiTree T) {
    if (T == NULL) return;
    BiTree Q[100];
    int front = 0, rear = 0;
    Q[rear++] = T;
    while (front < rear) {
        BiTree p = Q[front++];
        cout << p->data;
        if (p->lchild != NULL) Q[rear++] = p->lchild;
        if (p->rchild != NULL) Q[rear++] = p->rchild;
    }
}

6-7 递归统计二叉树中右孩子的个数
分数 10
作者 张瑞霞
单位 桂林电子科技大学
本题要求采用递归方式统计二叉树中右孩子结点的个数

函数接口定义：
在这里描述函数接口。例如：
int CountRightNode(BinTree bt);
其中bt是待统计的二叉树，函数返回右孩子结点的个数

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>
typedef char DataType;
typedef struct BTreeNode
{
    DataType data;
    struct BTreeNode *leftchild;
    struct BTreeNode *rightchild;
}BinTreeNode;
typedef BinTreeNode *BinTree;

BinTree CreateBinTree_Recursion()
{
    char ch;
    BinTree bt;
    scanf("%c", &ch);
    if (ch == '@')
        bt = NULL;
    else
    {
        bt = (BinTreeNode *)malloc(sizeof(BinTreeNode));
        bt->data = ch;
        bt->leftchild = CreateBinTree_Recursion();
        bt->rightchild = CreateBinTree_Recursion();
    }
    return bt;
}

/* 请在这里填写答案 */

void DestroyBinTree(BinTree bt)
{
    if (bt != NULL)
    {
        DestroyBinTree(bt->leftchild);
输入样例：
AB@D@@C@@
输出样例：
2
C (gcc)
/* === 答案代码块 === */
int CountRightNode(BinTree bt)
{
    if (bt == NULL)
        return 0;
    
    // 当前结点有右孩子则计数1，否则为0
    int count = (bt->rightchild != NULL) ? 1 : 0;
    
    // 递归统计：当前层计数 + 左子树右孩子数 + 右子树右孩子数
    return count + CountRightNode(bt->leftchild) + CountRightNode(bt->rightchild);
}

6-1 小孩报数（顺序循环队列版）
分数 10
作者 张庆
单位 集美大学
有若干个小孩围成一圈，现从指定的第1个开始报数，报到第 w个时，该小孩出列，然后从下一个小孩开始报数，仍是报到w个出列，如此重复下去，直到所有的小孩都出列（总人数不足w个时将循环报数），求小孩出列的顺序。
算法要求：使用顺序循环队列来存储所有小孩，报数时小孩出队，未数到w时，接着入队；数到w时，输出小孩的名字，该小孩不再入队，如此直到所有小孩出队，队列为空时停止报数。
请写出顺序循环队列的所有基本操作。
说明 ：参与报数游戏的小孩人数不能超过10人。

数据结构与操作函数接口定义：
typedef char ElemType;
typedef struct   // 顺序循环队列结点定义
{
    ElemType *name[MaxSize];   //小孩姓名
    int front,rear;        //队首和队尾指针
} SqQueue;
void InitQueue(SqQueue *&q);   //初始化队列；
void DestroyQueue(SqQueue *&q);  //销毁队列；
bool QueueEmpty(SqQueue *q);  //判定队列为空时返回true; 否则返回false;
bool enQueue(SqQueue *&q,ElemType *e);  // e 入队；成功入队返回true; 否则返回false;
bool deQueue(SqQueue *&q,ElemType *&e);  //出队，返回出队元素e，且成功出队返回true,否则返回false;
裁判测试程序样例：
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#define MaxSize 11
#define N 10

int main()
{
    ElemType *e;
    int n,i;
    SqQueue *q;
    InitQueue(q);    
    scanf("%d",&n);
    while(1)
    {
        char *name=(char *)malloc(sizeof(char)*N);
        scanf("%s",name);
        if( (strcmp("-1",name)==0)||!enQueue(q,name))
            break;
    }
    i=n-1;
    while(!QueueEmpty(q))
    {
        deQueue(q,e);
        if(i-->0) 
            enQueue(q,e);
        else
        {
            printf("%s\n",e);
            i=n-1;
            free(e);            
        }        
    }
    DestroyQueue(q);
}

/* 请在这里填写答案 */
输入样例：
第一行：报数w;
第二行：输入若干小孩姓名，以空格符间隔，以字符串“-1”结束输入。
在这里给出一组输入。例如：

3
Jenny Mike Lily Tom Yoyo -1

输出样例：
在这里给出相应的输出。例如：

Lily
Jenny
Yoyo
Mike
Tom

C++ (g++)
/* === 答案代码块 === */
// 初始化队列
void InitQueue(SqQueue *&q) {
    // 1. 为队列结构体分配内存
    q = (SqQueue *)malloc(sizeof(SqQueue));
    // 2. 初始化头尾指针，指向下标 0
    q->front = 0;
    q->rear = 0;
}

// 销毁队列
void DestroyQueue(SqQueue *&q) {
    // 释放 InitQueue 时 malloc 申请的内存
    free(q);
}

// 判定队列为空
bool QueueEmpty(SqQueue *q) {
    // 头尾指针重合即为空
    return (q->front == q->rear);
}

// 入队操作
bool enQueue(SqQueue *&q, ElemType *e) {
    // 1. 检查是否队满：(rear + 1) % MaxSize == front
    if ((q->rear + 1) % MaxSize == q->front) {
        return false;
    }
    // 2. 将数据存入 rear 指向的位置
    q->name[q->rear] = e;
    // 3. rear 指针逻辑后移一位
    q->rear = (q->rear + 1) % MaxSize;
    return true;
}

// 出队操作
bool deQueue(SqQueue *&q, ElemType *&e) {
    // 1. 检查是否队空
    if (q->front == q->rear) {
        return false;
    }
    // 2. 取出 front 指向的位置的数据给 e
    e = q->name[q->front];
    // 3. front 指针逻辑后移一位
    q->front = (q->front + 1) % MaxSize;
    return true;
}
7-1 递归实现逆序输出整数
分数 15
作者 张高燕
单位 浙大城市学院
本题目要求读入1个正整数n，然后编写递归函数reverse(int n)实现将该正整数逆序输出。

输入格式:
输入在一行中给出1个正整数n。

输出格式:
对每一组输入，在一行中输出n的逆序数。

输入样例:
12345
输出样例:
54321
C++ (g++)
#include <stdio.h>

/* === 答案代码块 === */
// 迭代版：直接一边算一边打印，解决”末尾为0”的问题
void reverse(int n) {
    // 处理特殊情况：如果输入就是 0
    if (n == 0) {
        printf("0");
        return;
    }
    
    // 你的 while 迭代思路
    while (n > 0) {
        int b = n % 10;  // 拿到最后一位（右边）
        printf("%d", b); // 直接打印，这样 120 就能打印出 021
        n = n / 10;      // 去掉最后一位（左边）
    }
}

int main() {
    int input = 0;
    // 修正 scanf 格式和变量声明
    if (scanf("%d", &input) == 1) {
        reverse(input);
    }
    return 0;
}
7-2 汉诺塔问题
分数 15
作者 董卫萍
单位 绍兴理工学院
相传在古印度圣庙中，有一种被称为汉诺塔(Hanoi)的游戏。该游戏是在一块铜板装置上，有三根杆(编号a、b、c)，在a杆自下而上、由大到小按顺序放置64个金盘(如图1)。游戏的目标：把a杆上的金盘全部移到c杆上，并仍保持原有顺序叠好。操作规则：每次只能移动一个盘子，并且在移动过程中三根杆上都始终保持大盘在下，小盘在上，操作过程中盘子可以置于a、b、c任一杆上。

汉诺.png

输入格式:
输入在一行中给出1个正整数n，表示盘子的个数。

输出格式:
输出搬动盘子过程，例如：No.x disk: y->z，表示移动第x号盘子从y柱子到z柱子。

输入样例:
在这里给出一组输入。例如：

3
输出样例:
在这里给出相应的输出。例如：

No.1 disk: a->c
No.2 disk: a->b
No.1 disk: c->b
No.3 disk: a->c
No.1 disk: b->a
No.2 disk: b->c
No.1 disk: a->c
C++ (g++)
#include <stdio.h>

/* === 答案代码块 === */
/**
 * 汉诺塔递归函数
 * n: 盘子数量
 * start: 起始柱子 (a)
 * aux: 中转柱子 (b)
 * end: 目标柱子 (c)
 */
void hanoi(int n, char start, char aux, char end) {
    // 停止条件：只剩一个盘子时，直接搬运，不再外包
    if (n == 1) {
        printf("No.1 disk: %c->%c\n", start, end);
        return;
    }

    // 第一步：把上面的 n-1 个盘子从 start 搬到 aux，借用 end
    // 注意：这里的参数位置发生了交换，因为这次的目标是 aux
    hanoi(n - 1, start, end, aux);

    // 第二步：把最底下那个最大的盘子（第 n 个）从 start 搬到 end
    printf("No.%d disk: %c->%c\n", n, start, end);

    // 第三步：把刚才放在 aux 上的 n-1 个盘子搬到 end，借用 start
    // 注意：这里的起始点变成了 aux，中转点变成了 start
    hanoi(n - 1, aux, start, end);
}

int main() {
    int n;
    // 读取输入的盘子数
    if (scanf("%d", &n) == 1) {
        // 调用递归：任务是从 a 搬到 c，借用 b
        hanoi(n, 'a', 'b', 'c');
    }
    return 0;
}
7-3 h0181. 约瑟夫问题
分数 10
作者 黄正鹏
单位 贵州工程应用技术学院
约瑟夫问题：有ｎ只猴子，按顺时针方向围成一圈选大王（编号从１到ｎ），从第１号开始报数，一直数到ｍ，数到ｍ的猴子退出圈外，剩下的猴子再接着从1开始报数。就这样，直到圈内只剩下一只猴子时，这个猴子就是猴王，编程求输入ｎ，ｍ后，输出最后猴王的编号。

输入格式:
每行是用空格分开的两个整数，第一个是 n, 第二个是 m ( 0 < m,n <=300)。最后一行是：

0 0

输出格式:
对于每行输入数据（最后一行除外)，输出数据也是一行，即最后猴王的编号

输入样例:
6 2
12 4
8 3
0 0
输出样例:
5
1
7
C++ (g++)
#include <stdio.h>
} SqQueue;

// 2. 把所有的函数实现挪到 main 的上面！！
/* === 答案代码块 === */
void InitQueue(SqQueue *&q) {
    q = (SqQueue *)malloc(sizeof(SqQueue));
    q->front = q->rear = 0;
}

bool QueueEmpty(SqQueue *q) {
    return (q->front == q->rear);
}

bool enQueue(SqQueue *&q, ElemType e) {
    if ((q->rear + 1) % MaxSize == q->front) return false;
    q->data[q->rear] = e; // 注意这里要用 data
    q->rear = (q->rear + 1) % MaxSize;
    return true;
}

bool deQueue(SqQueue *&q, ElemType &e) {
    if (q->front == q->rear) return false;
    e = q->data[q->front]; // 注意这里要用 data
    q->front = (q->front + 1) % MaxSize;
    return true;
}

// 3. 最后写 main 函数
int main() {
    int n, m;
    while (scanf("%d %d", &n, &m) == 2 && (n != 0 || m != 0)) {
        SqQueue *q;
        InitQueue(q);
        
        for (int i = 1; i <= n; i++) {
            enQueue(q, i);
        }

        int count = 0;
        ElemType e;
        // 只要人数 > 1 就继续
        while (((q->rear - q->front + MaxSize) % MaxSize) > 1) {
            deQueue(q, e);
            count++;
            if (count == m) {
                count = 0; // 出局，不入队
            } else {
                enQueue(q, e); // 没数到，回队尾
            }
        }
        
        deQueue(q, e);
        printf("%d\n", e);
        free(q);
    }
    return 0;
}
6-1 顺序栈操作-补充顺序栈入栈函数【可本地编译器调试】
分数 6
作者 CUIT通信DS课程组
单位 成都信息工程大学
本题要求实现一个顺序栈的入栈函数，可将字符压入到顺序栈中，如果成功，返回1，如果失败，返回0。

函数接口定义：
int Push (SqStack * S, DataType e);
其中 S 和 e 都是用户传入的参数。 S 是指向顺序栈的指针； e 是字符变量。如果入栈成功，返回1，如果失败，返回0。

裁判测试程序样例：
#include <stdio.h>
#include <malloc.h>
#include <string.h>

#define STACKSIZE 100                // 宏定义，设栈最大容量为100
typedef char DataType;                // 数据类型

/****** 顺序栈 ******/
typedef struct                        // 顺序栈定义
{
    DataType items[STACKSIZE];            
    int top;                        // top表示栈顶指针，取值范围-1—STACKSIZE-1
}SqStack;  

/* 【 本题要求函数-入栈 】*/
int Push (SqStack * S, DataType e);        
/*S为指向顺序栈的指针，e为待入栈的数据元素*/

/****** 顺序栈初始化 ******/
void Initstack(SqStack *stack)      // stack为指向顺序栈的指针
{
    stack->top = -1;
}

//出栈
int Pop (SqStack * S, DataType *e)       /*S指向顺序栈指针，e出栈元素*/   
{
    if( S->top <= -1)         /*栈为空*/
         return 0;
       *e= S->items[S->top];     /*将栈顶元素带回来*/
       S->top--;      /* 修改栈顶指针 */
       return 1;
}

/****** 主函数 ******/
int main()
{
    int i;                        
    SqStack stack;            // 顺序栈
    DataType ch;

    Initstack(&stack);
    for(i=0;i<STACKSIZE;i++)
    {
        ch = getchar();
        if(ch=='\n')
            break;
        if(!Push(&stack,ch))
            break;
    }

    if(Pop(&stack,&ch))
        printf("%c",ch);
        return 0;
}

/* 请在这里填写答案 */
输入样例：
在这里给出一组输入。例如：

asdfbdk

输出样例：
在这里给出相应的输出。例如：

k
C (gcc)
/* === 答案代码块 === */
int Push (SqStack * S, DataType e) {
    // 1. 判断栈是否已满
    // 因为 top 从 -1 开始，最大下标是 STACKSIZE - 1
    if (S->top >= STACKSIZE - 1) {
        return 0;
    }

    // 2. 先移动栈顶指针
    S->top++;

    // 3. 将元素存入新的栈顶位置
    // 直接使用 e，不要加 *
    S->items[S->top] = e;

    return 1;
}
6-2 用顺序栈实现将非负的十进制数转换为指定的进制数【有题解视频，可本地编译器调试】
分数 12
作者 CUIT通信DS课程组
单位 成都信息工程大学
利用顺序栈将输入的非负的十进制数N转换为指定的d（二、八或十六）进制数。

顺序栈的定义如下：
#define STACKSIZE  100  
typedef int DataType; 
typedef struct
{      
   DataType items[STACKSIZE];     /*存放栈中元素的一维数组*/
   int top;                    /*用来存放栈顶元素的下标*/
}SqStack;
函数接口定义：
int DecimalConvert(SqStack *s, int dec, int scale);
函数参数说明：形参--s、dec、scale，其中，s是存放转换后的scale进制数的各位数字，dec 主函数输入的待转换的十进制数，scale是指定的数制（只能是2、8或16）。 函数返回值：1，表示函数执行完成；0，表示函数未成功执行。

裁判测试程序样例：
#include <stdio.h>
{ // 初始化顺序栈
    S->top = -1;
    return 1;
}
int SqStackPush(SqStack* S, DataType e)
{ // 压栈函数
    if (S->top == STACKSIZE - 1)
        return 0;     /*栈已满*/
    S->top++;
    S->items[S->top] = e;

    return 1;
}
int SqStackPop(SqStack* S, DataType* e)
{ /* 将栈S的栈顶元素弹出，放到e所指的存储空间中 */
    if (S->top == -1)     /* 栈为空 */
        return 0;
    *e = S->items[S->top];     /* 将栈顶元素带回来 */
    S->top--;                    /* 修改栈顶指针 */

    return 1;
}
int SqStackEmpty(SqStack S)
{  /* S为顺序栈 */
    if (S.top == -1)
        return 1;
    else
        return 0;
}
/* 本题要求函数 */
int DecimalConvert(SqStack* s, int dec, int scale);

int main()
{
    SqStack s;
    char ch[] = "0123456789ABCDEF";  //二、八、十六进制所使用的数字
    unsigned dec, scale;
    DataType tmp;
    InitSqStack(&s);
    scanf("%d %d", &dec, &scale); // 某些编译器要求此处改为scanf_s
    if (DecimalConvert(&s, dec, scale))
    {
        printf("十进制数:%d,转换为:%d进制数,结果为:", dec, scale);
        while (!SqStackEmpty(s))
        {
            SqStackPop(&s, &tmp);
            printf("%c", ch[tmp]);
        }
    }
    else
        printf("数制转换未成功！");
    return 0;
}
/* 请在这里填写答案 */
输入样例：
20 2

输出样例：
十进制数:20,转换为:2进制数,结果为:10100
输入样例：
20 8

输出样例：
十进制数:20,转换为:8进制数,结果为:24
输入样例：
20 16

输出样例：
十进制数:20,转换为:16进制数,结果为:14
C (gcc)
/* === 答案代码块 === */
int DecimalConvert(SqStack *s, int dec, int scale) {
    // 处理特殊情况：如果输入的十进制数是 0
    if (dec == 0) {
        if (!SqStackPush(s, 0)) {
            return 0;
        }
        return 1;
    }

    // 只要待转换的数不为 0，就继续转换
    while (dec > 0) {
        // 1. 计算余数：dec % scale
        int remainder = dec % scale;

        // 2. 将余数压入栈中
        // 如果压栈失败（如栈满），则返回 0
        if (!SqStackPush(s, (DataType)remainder)) {
            return 0;
        }

        // 3. 更新 dec 为商：dec / scale，准备下一次迭代
        dec = dec / scale;
    }

    // 执行成功返回 1
    return 1;
}
7-1 判断回文
分数 15
作者 段华琼
单位 成都锦城学院
回文是指正读反读均相同的字符序列，如“abba”和“abdba”均是回文，但“good”不是回文。试写一个程序判定给定的字符向量是否为回文，用栈实现。(提示：将一半字符入栈)

输入格式:
输入任意字符串。

输出格式:
若字符串是回文，输出：xxxx是回文。
若字符串不是回文，输出：xxxx不是回文。

输入样例:
abba
输出样例:
abba是回文。
输入样例:
abdba
输出样例:
abdba是回文。
输入样例:
good
输出样例:
good不是回文。
C (gcc)
#include <stdio.h>
/* === 答案代码块 === */
// 初始化顺序栈 [cite: 181]
void InitSqStack(SqStack* S) {
    S->top = -1;
}

// 压栈操作 [cite: 195, 305]
int SqStackPush(SqStack* S, DataType e) {
    if (S->top == STACKSIZE - 1) return 0; // 栈满 [cite: 315]
    S->items[++(S->top)] = e;
    return 1;
}

// 出栈操作 [cite: 223, 313]
int SqStackPop(SqStack* S, DataType* e) {
    if (S->top == -1) return 0; // 栈空 [cite: 302]
    *e = S->items[(S->top)--];
    return 1;
}

int main() {
    SqStack s;
    InitSqStack(&s);
    char input[100];

    // 使用 fgets 读取整行，以支持包含空格的字符串
    if (fgets(input, sizeof(input), stdin) == NULL) return 0;

    // 去除 fgets 读入的末尾换行符 \n
    int n = strlen(input);
    if (n > 0 && input[n - 1] == '\n') {
        input[n - 1] = '\0';
        n--;
    }

    // 1. 将前半部分字符入栈 [cite: 31, 37]
    // 无论 n 是奇是偶，入栈个数均为 n/2
    for (int i = 0; i < n / 2; i++) {
        SqStackPush(&s, input[i]);
    }

    // 2. 确定后半部分比对的起点 [cite: 46]
    // 使用 (n + 1) / 2 可以完美跳过奇数长度的中间字符
    int start = (n + 1) / 2;
    int isPalindrome = 1; // 标志位：1表示是回文，0表示不是
    DataType temp;

    // 3. 依次弹出栈顶元素与后半部分比对 [cite: 31, 38]
    for (int i = start; i < n; i++) {
        SqStackPop(&s, &temp);
        if (temp != input[i]) {
            isPalindrome = 0; // 只要有一个不匹配，就不是回文
            break;
        }
    }

    // 4. 根据标志位输出结果
    if (isPalindrome) {
        printf("%s是回文。\n", input);
    } else {
        printf("%s不是回文。\n", input);
    }

    return 0;
}

6-1 求链式表的表长
分数 10
作者 陈越
单位 浙江大学
本题要求实现一个函数，求链式表的表长。

函数接口定义：
int Length( List L );
其中List结构定义如下：
typedef struct LNode *PtrToLNode;
struct LNode {
    ElementType Data;
    PtrToLNode Next;
};
typedef PtrToLNode List;
L是给定单链表，函数Length要返回链式表的长度。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct LNode *PtrToLNode;
struct LNode {
    ElementType Data;
    PtrToLNode Next;
};
typedef PtrToLNode List;

List Read(); /* 细节在此不表 */

int Length( List L );

int main()
{
    List L = Read();
    printf("%d\n", Length(L));
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
1 3 4 5 2 -1
输出样例：
5
C (gcc)
/* === 答案代码块 === */
int Length( List L ){
    List p=L;
    if(p==NULL ){
        return 0;
    }
    int i=1;
    while(p->Next!=NULL){
        i++;
        p= p->Next ;
    }
    return i;
}
6-2 统计专业人数
分数 10
作者 张泳
单位 浙大城市学院
本题要求实现一个函数，统计学生学号链表中专业为计算机的学生人数。链表结点定义如下：

struct ListNode {
    char code[8];
    struct ListNode *next;
};
这里学生的学号共7位数字，其中第2、3位是专业编号。计算机专业的编号为02。

函数接口定义：
int countcs( struct ListNode *head );
其中head是用户传入的学生学号链表的头指针；函数countcs统计并返回head链表中专业为计算机的学生人数。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    char code[8];
    struct ListNode *next;
};

struct ListNode *createlist(); /*裁判实现，细节不表*/
int countcs( struct ListNode *head );

int main()
{
    struct ListNode  *head;

    head = createlist();
    printf("%d\n", countcs(head));
    
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
1021202
2022310
8102134
1030912
3110203
4021205
#
输出样例：
3
C (gcc)
/* === 答案代码块 === */
int countcs( struct ListNode *head ){
    struct ListNode *p=head;
    if(p == NULL ){
        return 0;
    }
    int count=0;
    int i=1;
    if(p->next==NULL){
        if(p->code[i]=='0'){
            i++;
            if(p->code[i]=='2'){
                count++;
            }
        }
        return count;
    }
    while(p->next!=NULL){
        i=1;
        if(p->code[i]=='0'){
            i++;
            if(p->code[i]=='2'){
                count++;
            }
        }
        p=p->next;
    }
    i=1;
    if(p->next==NULL){
        if(p->code[i]=='0'){
            i++;
            if(p->code[i]=='2'){
                count++;
            }
        }
    }
    return count;
}
6-3 带头结点的单链表插入操作
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现带头结点的单链表插入操作，插入成功返回1，否则返回0。

函数接口定义：
int insert_link ( LinkList L,int i,ElemType e);
L是单链表的头指针，i为插入位置，e是插入的数据元素，插入成功返回1，否则返回0。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef int ElemType;
typedef struct LNode
{
    ElemType data;
    struct LNode *next;
}LNode,*LinkList;

LinkList Create();/* 细节在此不表 */
void print( LinkList L);
int insert_link ( LinkList L,int i,ElemType e);
 
int main()
{
    int position,insert_data;int flag;
    LinkList L = Create();
    scanf("%d",&position);
    scanf("%d",&insert_data);    
    flag=insert_link(L,position,insert_data);
    if(flag) 
    {
        print(L);
    }
    else 
    { 
        printf("Wrong Position for Insertion");
    }
    return 0;
}
void print(LinkList L)
{ 
    LinkList p;
    p=L->next;
    while (p)
    {
         printf("%d ", p->data);
         p =p->next;
    }
}
/* 请在这里填写答案 */
输入格式：
输入数据为三行，第一行是若干正整数，最后以-1表示结尾（-1不算在序列内，不要处理）。所有数据之间用空格分隔。
第二行数据是插入位置，第三行数据是被插入元素值。

输入样例：
1 2 3 4 5 6 -1
2 
100
输出样例：
1 100 2 3 4 5 6 
C (gcc)
/* === 答案代码块 === */
int insert_link ( LinkList L,int i,ElemType e){
    if(L==NULL || i<=0){
        return 0;
    }
    LinkList p;
    p=L;
    for(int j=0;j<i-1;j++){
        p=p->next;
        if(p == NULL){
            return 0;
        }
    }
    LNode *s = (LNode *)malloc(sizeof(LNode));
    s->data=e;
    s->next=p->next;
    p->next=s;
    return L;
}
6-4 递增的整数序列链表的插入
分数 10
作者 DS课程组
单位 浙江大学
本题要求实现一个函数，在递增的整数序列链表（带头结点）中插入一个新整数，并保持该序列的有序性。

函数接口定义：
List Insert( List L, ElementType X );
其中List结构定义如下：
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data; /* 存储结点数据 */
    PtrToNode   Next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */
L是给定的带头结点的单链表，其结点存储的数据是递增有序的；函数Insert要将X插入L，并保持该序列的有序性，返回插入后的链表头指针。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data;
    PtrToNode   Next;
};
typedef PtrToNode List;

List Read(); /* 细节在此不表 */
void Print( List L ); /* 细节在此不表 */

List Insert( List L, ElementType X );

int main()
{
    List L;
    ElementType X;
    L = Read();
    scanf("%d", &X);
    L = Insert(L, X);
    Print(L);
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
5
1 2 4 5 6
3
输出样例：
1 2 3 4 5 6 
C (gcc)
/* === 答案代码块 === */
List Insert( List L, ElementType X ){
    List p = L;
    List s = (List)malloc(sizeof(struct Node));
    s->Data = X;
    
    // 常规逻辑直接兼容空链表的情况
    while(p->Next != NULL && X > p->Next->Data){
        p = p->Next;
    }
    
    s->Next = p->Next;
    p->Next = s;
    
    return L;
}
6-5 删除单链表偶数节点
分数 10
作者 C课程组
单位 浙江大学
本题要求实现两个函数，分别将读入的数据存储为单链表、将链表中偶数值的结点删除。链表结点定义如下：

struct ListNode {
    int data;
    struct ListNode *next;
};
函数接口定义：
struct ListNode *createlist();
struct ListNode *deleteeven( struct ListNode *head );
函数createlist从标准输入读入一系列正整数，按照读入顺序建立单链表。当读到−1时表示输入结束，函数应返回指向单链表头结点的指针。

函数deleteeven将单链表head中偶数值的结点删除，返回结果链表的头指针。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist();
struct ListNode *deleteeven( struct ListNode *head );
void printlist( struct ListNode *head )
{
     struct ListNode *p = head;
     while (p) {
           printf("%d ", p->data);
           p = p->next;
     }
     printf("\n");
}

int main()
{
    struct ListNode *head;

    head = createlist();
    head = deleteeven(head);
    printlist(head);

    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
1 2 2 3 4 5 6 7 -1
输出样例：
1 3 5 7 
C (gcc)
/* === 答案代码块 === */
struct ListNode *createlist() {
    int val;
    struct ListNode *head = NULL, *tail = NULL;
    while (scanf("%d", &val) && val != -1) {
        struct ListNode *s = (struct ListNode *)malloc(sizeof(struct ListNode));
        s->data = val;
        s->next = NULL;
        if (head == NULL)
            head = tail = s;
        else {
            tail->next = s;
            tail = s;
        }
    }
    return head;
}

struct ListNode *deleteeven(struct ListNode *head) {
    // 删掉头部连续的偶数结点
    while (head != NULL && head->data % 2 == 0) {
        struct ListNode *tmp = head;
        head = head->next;
        free(tmp);
    }
    if (head == NULL) return NULL;

    // 删掉中间和尾部的偶数结点
    struct ListNode *p = head;
    while (p->next != NULL) {
        if (p->next->data % 2 == 0) {
            struct ListNode *tmp = p->next;
            p->next = tmp->next;
            free(tmp);
        } else {
            p = p->next;
        }
    }
    return head;
}
6-6 逆序数据建立链表
分数 10
作者 C课程组
单位 浙江大学
本题要求实现一个函数，按输入数据的逆序建立一个链表。

函数接口定义：
struct ListNode *createlist();
函数createlist利用scanf从输入中获取一系列正整数，当读到−1时表示输入结束。按输入数据的逆序建立一个链表，并返回链表头指针。链表节点结构定义如下：
struct ListNode {
    int data;
    struct ListNode *next;
};
裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist();

int main()
{
    struct ListNode *p, *head = NULL;

    head = createlist();
    for ( p = head; p != NULL; p = p->next )
        printf("%d ", p->data);
    printf("\n");

    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
1 2 3 4 5 6 7 -1
输出样例：
7 6 5 4 3 2 1 
C (gcc)
#include <stdio.h>
#include <stdlib.h>

/* === 答案代码块 === */
struct ListNode *createlist() {
    struct ListNode *head = NULL; // 初始化头指针为空
    int val;

    // 持续读入数据，直到读到 -1
    while (scanf("%d", &val) && val != -1) {
        // 1. 为新节点分配内存
        struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
        if (newNode == NULL) return NULL; // 内存分配失败处理

        // 2. 赋值
        newNode->data = val;

        // 3. 执行头插逻辑
        // 新节点的 next 指向当前的头节点
        newNode->next = head;
        // 更新头指针，使新节点成为新的表头
        head = newNode;
    }

    return head;
}
6-7 两个有序链表序列的合并
分数 15
作者 DS课程组
单位 浙江大学
本题要求实现一个函数，将两个链表表示的递增整数序列合并为一个非递减的整数序列。

函数接口定义：
List Merge( List L1, List L2 );
其中List结构定义如下：
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data; /* 存储结点数据 */
    PtrToNode   Next; /* 指向下一个结点的指针 */
};
typedef PtrToNode List; /* 定义单链表类型 */
L1和L2是给定的带头结点的单链表，其结点存储的数据是递增有序的；函数Merge要将L1和L2合并为一个非递减的整数序列。应直接使用原序列中的结点，返回归并后的带头结点的链表头指针。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

typedef int ElementType;
typedef struct Node *PtrToNode;
struct Node {
    ElementType Data;
    PtrToNode   Next;
};
typedef PtrToNode List;

List Read(); /* 细节在此不表 */
void Print( List L ); /* 细节在此不表；空链表将输出NULL */

List Merge( List L1, List L2 );

int main()
{
    List L1, L2, L;
    L1 = Read();
    L2 = Read();
    L = Merge(L1, L2);
    Print(L);
    Print(L1);
    Print(L2);
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
3
1 3 5
5
2 4 6 8 10
输出样例：
1 2 3 4 5 6 8 10 
NULL
NULL
C (gcc)
/* === 答案代码块 === */
List Merge(List L1, List L2) {
    // 1. 创建结果链表的头节点
    List L = (List)malloc(sizeof(struct Node));
    L->Next = NULL;
    
    PtrToNode tail = L;      // 始终指向结果链表的末尾
    PtrToNode p1 = L1->Next; // 跳过 L1 的头节点，指向第一个有效节点
    PtrToNode p2 = L2->Next; // 跳过 L2 的头节点，指向第一个有效节点

    // 2. 归并过程
    while (p1 != NULL && p2 != NULL) {
        if (p1->Data <= p2->Data) {
            // p1 较小，接入 tail 后
            tail->Next = p1;
            p1 = p1->Next;
        } else {
            // p2 较小，接入 tail 后
            tail->Next = p2;
            p2 = p2->Next;
        }
        tail = tail->Next; // 移动 tail 指针
    }

    // 3. 处理剩余部分
    if (p1 != NULL) {
        tail->Next = p1;
    } else {
        tail->Next = p2;
    }

    // 4. 题目要求合并后 L1 和 L2 的头节点指向 NULL
    L1->Next = NULL;
    L2->Next = NULL;

    return L;
}
6-8 链表逆置
分数 10
作者 张泳
单位 浙大城市学院
本题要求实现一个函数，将给定单向链表逆置，即表头置为表尾，表尾置为表头。链表结点定义如下：

struct ListNode {
    int data;
    struct ListNode *next;
};
函数接口定义：
struct ListNode *reverse( struct ListNode *head );
其中head是用户传入的链表的头指针；函数reverse将链表head逆置，并返回结果链表的头指针。

裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>

struct ListNode {
    int data;
    struct ListNode *next;
};

struct ListNode *createlist(); /*裁判实现，细节不表*/
struct ListNode *reverse( struct ListNode *head );
void printlist( struct ListNode *head )
{
     struct ListNode *p = head;
     while (p) {
           printf("%d ", p->data);
           p = p->next;
     }
     printf("\n");
}

int main()
{
    struct ListNode  *head;

    head = createlist();
    head = reverse(head);
    printlist(head);
    
    return 0;
}

/* 你的代码将被嵌在这里 */
输入样例：
1 2 3 4 5 6 -1
输出样例：
6 5 4 3 2 1 
C (gcc)
/* === 答案代码块 === */
struct ListNode *reverse(struct ListNode *head) {
    struct ListNode *prev = NULL;    // 指向前驱节点
    struct ListNode *curr = head;    // 指向当前正在处理的节点
    struct ListNode *next = NULL;    // 用于暂存后继节点，防止断链

    while (curr != NULL) {
        // 1. 记录当前节点的下一个节点
        next = curr->next;
        
        // 2. 核心操作：将当前节点的 next 指向它的前驱
        curr->next = prev;
        
        // 3. 两个辅助指针整体向后移动一位
        prev = curr;
        curr = next;
    }

    // 当 curr 为空时，prev 恰好指向原链表的最后一个节点，即逆置后的新头节点
    return prev;
}

6-1 顺序表的插入操作
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，在顺序表的第i个位置插入一个新的数据元素e，插入成功后顺序表的长度加1，函数返回值为1；插入失败函数返回值为0；

函数接口定义：
int ListInsert(SqList &L,int i,ElemType e);
其中SqList结构定义如下：
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 5
typedef int ElemType;
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
void InitList(SqList &L);/*细节在此不表*/
int ListInsert(SqList &L,int i,ElemType e);
int main()
{
    SqList L;
    InitList(L);
    ElemType e;
    int i;
    scanf("%d%d",&i,&e);
    int result=ListInsert(L,i,e);
    if(result==0){
        printf("Insertion Error.The value of i is unlawful or the storage space is full!");    
    }else if(result==1){
        printf("Insertion Success.The elements of the SequenceList L are:");    
        for(int j=0;j<L.length;j++){
            printf(" %d",L.elem[j]);
        }
    }
    return 0;
}
/* 请在这里填写答案 */

输入格式：
输入数据有1行，首先给出以-1结束的顺序表元素值（不超过100个，-1不属于顺序表元素），然后是插入位置和被插入元素值。所有数据之间用空格分隔。

输入样例：
2 6 4 -1 2 100

输出样例：
Insertion Success.The elements of the SequenceList L are: 2 100 6 4

C++ (g++)
/* === 答案代码块 === */
int ListInsert(SqList &L, int i, ElemType e) {
    // 1. 检查位置是否合法：i < 1 (太前) 或 i > L.length + 1 (太后)
    // 同时题目给定 MAXSIZE 是 5，如果当前长度已经达到 5，也无法插入
    if (i < 1 || i > L.length + 1 || L.length >= MAXSIZE) {
        return 0; // 插入失败，返回 0
    }

    // 2. 腾位置：从顺序表最后一个人开始，每个人往后退一格
    // j 是当前人的下标，最后一个人下标是 L.length - 1
    // 循环直到腾出第 i 个位置（下标为 i-1）为止
    for (int j = L.length - 1; j >= i - 1; j--) {
        L.elem[j + 1] = L.elem[j]; // 把 j 位置的元素搬到 j+1
    }

    // 3. 插入新元素：现在下标 i-1 的位置已经空出来了
    L.elem[i - 1] = e;

    // 4. 更新记录：表长记得加 1
    L.length++;

    return 1; // 插入成功，返回 1
}

6-2 顺序表的有序插入操作
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，要求将指定元素插入到有序表的合适位置，使得插入后仍然保持有序，若插入失败返回0；插入成功则返回1，并且顺序表的长度加1.

函数接口定义：
int SqInsert(SqList &L,ElemType e);
其中SqList结构定义如下：
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 5
typedef int ElemType;
typedef struct{
    ElemType *elem;
    int length;
}SqList;
void InitList(SqList &L);/*函数的实现此处不再显示*/
int SqInsert(SqList &L,ElemType e);
int main()
{
    SqList L;
    InitList(L);
    ElemType e;
    scanf("%d",&e);
    int result=SqInsert(L,e);
    if(result==0){
        printf("Insertion Error.The storage space is full!");    
    }else if(result==1){
        printf("Insertion Success.The elements of the SequenceList L are:");    
        for(int j=0;j<L.length;j++){
            printf(" %d",L.elem[j]);
        }
    }
    return 0;
}
   
/* 请在这里填写答案 */
输入格式：
输入数据有1行，首先给出以-1结束的非递减顺序表元素值（不超过100个，-1不属于顺序表元素，），然后是被插入元素值。所有数据之间用空格分隔。

输入样例：
4 8 20 -1 10 

输出样例：
Insertion Success.The elements of the SequenceList L are: 4 8 10 20

C++ (g++)
/* === 答案代码块 === */
int SqInsert(SqList &L,ElemType e){
    if(L.length>=MAXSIZE){
        return 0;
    }
    L.length++;
    L.elem[L.length-1]=2147483647;
    for(int i=0;i<L.length;i++){
        if(L.elem[i]>e){
            for(int j=0;j<L.length-i;j++){
                L.elem[L.length-j]=L.elem[L.length-1-j];
            }
            L.elem[i]=e;
            return 1;
        }
    }
}
6-3 顺序表的删除操作
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，要求将顺序表的第i个元素删掉，成功删除返回1，否则返回0； 

函数接口定义：
int ListDelete(SqList &L,int i);
其中SqList结构定义如下：
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
裁判测试程序样例：
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 5
typedef int ElemType;
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
void InitList(SqList &L);/*细节在此不表*/
int ListDelete(SqList &L,int i);
int main()
{
    SqList L;
    InitList(L);
    int i;
    scanf("%d",&i);
    int result=ListDelete(L,i);
    if(result==0){
        printf("Delete Error.The value of i is illegal!");    
    }else if(result==1){
        printf("Delete Success.The elements of the SequenceList L are:");    
        for(int j=0;j<L.length;j++){
            printf(" %d",L.elem[j]);
        }
    }
    return 0;
}
/* 请在这里填写答案 */
输入格式：
输入数据有1行，首先给出以-1结束的顺序表元素值（不超过100个，-1不属于顺序表元素），然后是删除位置。所有数据之间用空格分隔。

输入样例：
2 6 4 -1 1

输出样例：
Delete Success.The elements of the SequenceList L are: 6 4

C++ (g++)
/* === 答案代码块 === */
int ListDelete(SqList &L,int i){
    if (i < 1 || i > L.length) {
        return 0;
    }
    for(int j=i;j<L.length;j++){
        L.elem[j-1]=L.elem[j];
    }
    L.length--;
    return 1;
}
6-4 顺序表的查找操作
分数 10
作者 DS课程组
单位 临沂大学
本题要求实现一个函数，要求从顺序表中查找指定元素，并返回第一个查找成功的元素在表中的位置序号，若查找失败，则返回0；

函数接口定义：
int LocateElem(SqList L,ElemType e);
其中SqList结构定义如下：
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
    ```

### 裁判测试程序样例：
```c++
#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 5
typedef int ElemType;
typedef struct{
    ElemType *elem;
    int length;
 }SqList;
void InitList(SqList &L);/*细节在此不表*/
int LocateElem(SqList L,ElemType e);

int main()
{
    SqList L;
    InitList(L);
    ElemType e;
    int p;
    scanf("%d",&e);
    p=LocateElem(L,e);
    printf("The position of %d in SequenceList L is %d.",e,p);
    return 0;
}

/* 请在这里填写答案 */
输入格式：
输入数据有1行，首先给出以-1结束的顺序表元素值（不超过100个，-1不属于顺序表元素），然后是待查找的元素值。所有数据之间用空格分隔。

输入样例：
2 6 4 9 13 -1 2

输出样例：
The position of 2 in SequenceList L is 1.

C++ (g++)
/* === 答案代码块 === */
int LocateElem(SqList L,ElemType e){
    for(int i=0;i<L.length;i++){
        if(L.elem[i]==e){
            return i+1;
        }
        
    }
    return 0;
}
