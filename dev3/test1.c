#include<stdio.h> 
#include<string.h>
#include<stdlib.h>

typedef struct _test {
  float size; 
  struct _test* next;
  void* point;
} elem;

typedef struct {
  int    field_a;
  int    field_b;
  int    field_c;
  float  field_d;
  void*  field_e;
  char*  field_f;
} big;

void main(){
    big b;
    elem* head, tmp;
    char bla[]="Saturn";

    b.field_a = 2;
    b.field_b = 5;
    b.field_c = 1000;
    b.field_d = 3.14;
    b.field_e = &b.field_b;
    b.field_f = (char*)malloc(strlen(bla));
    strncpy(b.field_f,bla, strlen(bla));

    head = (elem*) malloc(sizeof(elem));
    head->size = 2.0;
    head->point = &b.field_a;
    head->next = (elem*) malloc(sizeof(elem));
    head->next->size = 4;
    head->next->point = &b.field_b;
    head->next->next = (elem*) malloc(sizeof(elem));
    head->next->next->size = 8;
    head->next->next->point = &b.field_c;
    head->next->next->next = 0;

    printf("done");
}

