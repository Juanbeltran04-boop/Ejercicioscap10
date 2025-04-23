%{
#include "parser.tab.h"
%}

%%
dos      return DOS;
tres     return TRES;
cuatro   return CUATRO;
cinco    return CINCO;
seis     return SEIS;
uno      return UNO;
[ \t\n]+ ;  // Ignorar espacios, tabulaciones y saltos de línea
.        return yytext[0];
%%

int yywrap(void) {
    return 1;
}
