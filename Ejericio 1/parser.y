%{
#include <stdio.h>
#include <stdlib.h>

// Declaraciones necesarias
int yylex(void);
void yyerror(char *s);
%}

%token DOS TRES CUATRO CINCO SEIS UNO

%%
S  : A B C
   | D E
   ;

A  : DOS B TRES
   | /* ε */
   ;

B  : /* ε */ B1
   ;

B1 : CUATRO C CINCO B1
   | /* ε */
   ;

C  : SEIS A B
   | /* ε */
   ;

D  : UNO A E
   ;

E  : TRES
   ;
%%

int main() {
    printf("Usuario, para comenzar ingresa una cadena\n");
    yyparse();
    printf("Cadena válida.\n");
    return 0;
}

void yyerror(char *s) {
    fprintf(stderr, "Error de sintaxis: %s\n", s);
}
