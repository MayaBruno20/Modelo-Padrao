# Modelo-Padrao
Código de estudo em python.

O Modelo Padrão é uma teoria da física que descreve as particulas elementares e a forma que interagem entre si. Neste código, realizei a conversão da fórmula para simular a interação de partículas carregadas (elétrons e prótons) em um campo elétrico, calculando as forças elétricas sobre elas.


Este código Python define duas classes: Particle e ElectricField, e usa essas classes para calcular a força elétrica sobre elétrons e prótons em um campo elétrico.

A classe Particle representa uma partícula com uma carga e uma massa específicas.
A classe ElectricField representa um campo elétrico com uma força específica.
O método force_on_particle da classe ElectricField calcula a força elétrica sobre uma partícula dada a sua carga e a força do campo elétrico.

- A classe Particle tem um construtor __init__ que inicializa os atributos charge (carga) e mass (massa) para uma partícula.
- A classe ElectricField tem um construtor __init__ que define o atributo strength (força) para representar a força do campo elétrico.
- O método force_on_particle calcula a força elétrica sobre uma partícula, multiplicando a carga da partícula pela força do campo elétrico.
- Duas instâncias de Particle são criadas: electron com carga -1 e massa 1 (em unidades de massa de elétron) e proton com carga 1 e massa 1836 (em unidades de massa de elétron).
- Uma instância de ElectricField é criada com uma força padrão de 1.0.
- A força sobre cada partícula é calculada usando o método force_on_particle da classe ElectricField.
- Finalmente, as forças calculadas são impressas na tela.
