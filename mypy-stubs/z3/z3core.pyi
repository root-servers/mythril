from .z3types import Ast, ContextObj

def Z3_mk_eq(ctx: ContextObj, a: Ast, b: Ast) -> Ast: ...
def Z3_mk_div(ctx: ContextObj, a: Ast, b: Ast) -> Ast: ...
