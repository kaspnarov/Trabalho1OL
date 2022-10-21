from ortools.linear_solver import pywraplp

# Instancia um solver Glop.
solver = pywraplp.Solver.CreateSolver('GLOP')

# Cria as variáveis que terão qualquer valor não-negativo.
S1 = solver.NumVar(0, solver.infinity() , 'S1')
S2 = solver.NumVar(0, solver.infinity() , 'S2')
S3 = solver.NumVar(0, solver.infinity() , 'S3')

G1 = solver.NumVar(0, solver.infinity() , 'G1')
G2 = solver.NumVar(0, solver.infinity() , 'G2')
G3 = solver.NumVar(0, solver.infinity() , 'G3')

R1 = solver.NumVar(0, solver.infinity() , 'R1')
R2 = solver.NumVar(0, solver.infinity() , 'R2')
R3 = solver.NumVar(0, solver.infinity() , 'R3')

# Equações de restrição:
solver.Add(S1 + S2 + S3 == 2500000)
solver.Add(G1 + G2 + G3 == 1000000)
solver.Add(R1 + R2 + R3 == 1700000)

solver.Add(S1 + G1 + R1 <= 3000000)
solver.Add(S2 + G2 + R2 <= 3000000)
solver.Add(S3 + G3 + R3 <= 3000000)

# Função objetivo.
solver.Minimize(8*((S1 * 0.05)/(1-((1+0.05)**(-8))) + (S2 * 0.052)/(1-((1+0.052)**(-8))) + (S3 * 0.055)/(1-((1+0.055)**(-8))) + 
                (G1 * 0.065)/(1-((1+0.065)**(-8))) + (G2 * 0.062)/(1-((1+0.062)**(-8))) + (G3 * 0.058)/(1-((1+0.058)**(-8))) + 
                (R1 * 0.061)/(1-((1+0.061)**(-8))) + (R2 * 0.062)/(1-((1+0.062)**(-8))) + (R3 * 0.065)/(1-((1+0.065)**(-8)))))

# Resolve o sistema.
solver.Solve()

# Mostra os resultados.
print('Solution:')
print('z = %.2f' % solver.Objective().Value())

print(' ̲ ̲|̲____S̲_____|̲____G̲____|̲____R̲____')
print('1 |  %d |    %d    | %d' % (S1.solution_value(), G1.solution_value(), R1.solution_value()))
print('2 |     %d    |    %d    | %d' % (S2.solution_value(), G2.solution_value(), R2.solution_value()))
print('3 |     %d    | %d |    %d' % (S3.solution_value(), G3.solution_value(), R3.solution_value()))
    
