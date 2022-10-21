from ortools.linear_solver import pywraplp

# Instancia um solver Glop.
solver = pywraplp.Solver.CreateSolver('GLOP')


# Cria as variáveis que terão qualquer valor entre 5000 e 40000, inclusive.
a = solver.NumVar(5000, 40000, 'a')
b = solver.NumVar(5000, 40000, 'b')
c = solver.NumVar(5000, 40000, 'c')
d = solver.NumVar(5000, 40000, 'd')
e = solver.NumVar(5000, 40000, 'e')
f = solver.NumVar(5000, 40000, 'f')

# Equações de restrição:
solver.Add(a + b + c + d + e + f == 100000)
solver.Add(b + c + e + f == 50000)
solver.Add(a + b + c <= 30000)

# Função objetivo:
solver.Maximize(0.053 * a + 0.062 * b + 0.051 * c + 0.049 * d + 0.065 * e + 0.034 * f)

# Resolve o sistema.
solver.Solve()

# Mostra os resultados.
print('Solution:')
print('z =', solver.Objective().Value())
print(' ̲ ̲ ̲ ̲ ̲a̲ ̲ ̲ ̲ ̲|̲ ̲ ̲ ̲b ̲ ̲ ̲ ̲|̲ ̲ ̲ ̲c ̲ ̲ ̲ ̲|̲ ̲ ̲ ̲ ̲d ̲ ̲ ̲ ̲|̲ ̲ ̲ ̲ ̲e ̲ ̲ ̲ ̲|̲ ̲ ̲ ̲f ̲ ̲ ̲ ̲')
print(' ', a.solution_value(), '|', b.solution_value(), '|', c.solution_value(), '|', d.solution_value(), '|', e.solution_value(), '|', f.solution_value())


