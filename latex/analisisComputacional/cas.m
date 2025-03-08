% Definir la función
f = @(x) sin(sqrt(x));

% Límites de integración
a = 0;
b = 10;
n = 5; % Número de subintervalos

% Ancho de los subintervalos
dx = (b - a) / n;

% Seleccionar el método ('izq', 'der' o 'med')
metodo = 'med'; % Cambiar a 'izq', 'der' o 'med'

% Puntos de evaluación según el método
if strcmp(metodo, 'izq')
    x = linspace(a, b - dx, n);
elseif strcmp(metodo, 'der')
    x = linspace(a + dx, b, n);
elseif strcmp(metodo, 'med')
    x = linspace(a + dx/2, b - dx/2, n);
else
    error('Método no reconocido. Usa "izq", "der" o "med".');
end

% Evaluar la función y calcular la suma de Riemann
y = f(x);
areas = y * dx; % Áreas de cada rectángulo
suma = sum(areas);

% Imprimir la tabla de valores
fprintf('\nTabla de Valores - Suma de Riemann (%s)\n', metodo);
fprintf('--------------------------------------------------\n');
fprintf('|  i  |    x_i    |   f(x_i)   |  f(x_i) * dx  |\n');
fprintf('--------------------------------------------------\n');

for i = 1:n
    fprintf('| %2d  | %8.4f | %9.4f | %12.6f |\n', i, x(i), y(i), areas(i));
end

fprintf('--------------------------------------------------\n');
fprintf('Aproximación de la integral (%s): %.6f\n\n', metodo, suma);

% Crear la gráfica
figure;
hold on;

% Dibujar los rectángulos
for i = 1:n
    if strcmp(metodo, 'izq')
        xi = x(i);
    elseif strcmp(metodo, 'der')
        xi = x(i) - dx;
    elseif strcmp(metodo, 'med')
        xi = x(i) - dx/2;
    end

    % Dibujar el rectángulo
    rectangle('Position', [xi, 0, dx, y(i)], 'FaceColor', [0.9, 0.9, 0.9], 'EdgeColor', 'r');
end

% Dibujar la función sobre los rectángulos
x_plot = linspace(a, b, 1000);
plot(x_plot, f(x_plot), 'b', 'LineWidth', 2);

% Etiquetas y título
xlabel('x');
ylabel('f(x)');
title(['Suma de Riemann - Método: ', metodo]);
grid on;
hold off;

