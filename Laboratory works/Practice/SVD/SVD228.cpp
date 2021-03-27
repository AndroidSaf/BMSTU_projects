// ConsoleApplication4.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

//Singular Value Decomposition
#include "pch.h"
#include <iostream> 
#include <iomanip>

using namespace std;
inline double square(double x) { return x * x; }  //Функция возведения числа в квадрат

int main()
{
	setlocale(LC_ALL, "ru");
	//Объявление переменных
	const int a = 100; //Количество строк и столбцов
	double A [a][a]; 
	double At [a][a];
	double AtA [a][a];
	double E [a][a];
	double L [a];
	double X [a];
	double U [a][a];
	double V [a][a];
	double Q [a][a];
	double R [a][a];
	double R1 [a][a];
	double T [a][a];

	//Задание параметров исходной матрицы (строк и столбцов)
	cout << " Enter size of Matrix A" << endl;
	cout << endl;
	int n, m;
	cout << " rows = ";
	cin >> m;
	cout << " colums = ";
	cin >> n;
	cout << endl;
	

	//Ввод Матрицы А
	cout << " Enter Matrix A\n";
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << " A[" << i << "][" << j << "] = ";
			cin >> A[i][j];
			//A[i][j] = rand() % 10;
		}
	}
	cout << endl;

	//Транспанируем Матрицу A
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			At[j][i] = A[i][j];
		}
	}

	//Выводим  Матрицу А
	cout << " Matrix A\n";
	cout << endl;
	for (int i = 0; i < m; i++)
	{
		for (int j = 0; j < n; j++)
		{
			cout << setw(3) << A[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;

	//Выводим транспанированную матрицу А
	cout << " Transposition Matrix A\n";
	cout << endl;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < m; j++)
		{
			cout << At[i][j] << "\t";
		}
		cout << endl;
	}
	cout << endl;

	if (m >= n)
	{
		//Перемножение транспанированной матрицы А на матрицу А
		cout << " Matrix At*A\n";
		cout << endl;
		double w = 0;
		double p = 1;
		for (int i = 0; i < n; i++)
		{
			for (int l = 0; l < n; l++)
			{
				for (int j = 0; j < m; j++)
				{
					p = At[i][j] * A[j][l];
					w += p;
				}
				AtA[i][l] = w;
				w = 0;
			}
		}

		//Выводим  Матрицу AtA
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << AtA[i][j] << "\t";
			}
			cout << endl;
		}
		cout << endl;

		//Перенос данных матрицы AtA в дополнительную
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				R[i][j] = AtA[i][j];
			}
		}

		//Нахождение собственных чисел матрицы через QR - разложение  
		int vs = 1; //Сумма элементов, не лежащих на главной диагонали
		double c, s; //c - косинус угла поворота; s - синус угла поворота
		int k = 0;
		double ww = 0;
		double pt = 1;

		//Цикл для вывода собственных чисел матрицы на её главной диагонали
		while (vs != 0)
		{

			//Создание единичной матрицы (начальный вид ортогональной матрицы)
		  for (int i = 0; i < n; i++)
		  {
			 for (int j = 0; j < n; j++)
			 {
				if (i == j)
					E[i][j] = 1;
				else
					E[i][j] = 0;
			 }
		  }

		    //Получение QR-разложения для матрицы AtA
			for (int l = 0; l < n - 1; l++)
			{
				for (int i = l + 1; i < n; i++)
				{
					//cout << endl;
					//cout << "Matrix Rotation " << k + 1 << endl;
					//cout << endl;
					c = R[l][l] / sqrt(square(R[l][l]) + square(R[i][l]));  //Значение косинуса
					s = R[i][l] / sqrt(square(R[l][l]) + square(R[i][l]));  //Значение синуса

					//Составляем матрицу вращений Гивенса T для матрицы AtA 
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							if (((e == f) && (e == l)) || ((e == f) && (e == i)))
								T[e][f] = c;
							else
								if ((e != f) && (e == i) && (f == l))
									T[e][f] = -s;
								else
									if ((e != f) && (e == l) && (f == i))
										T[e][f] = s;
									else
										if (e == f)
											T[e][f] = 1;
										else
											if (e != f)
												T[e][f] = 0;
							//cout << setw(10) << T[e][f] << "\t";
						}
						//cout << endl;
					}

					//Постепенное обнуление столбцов под главной изменяемой матрицы AtA 
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{

							//Перемножение матрицы вращений на изменяемую матрицу AtA
							for (int j = 0; j < n; j++)
							{
								pt = T[e][j] * R[j][f]; 
								ww += pt;
							}
							R1[e][f] = ww;
							ww = 0;
							pt = 1;

							//Составление ортогональной матрицы путем перемножения полученной матрицы вращения на предыдущую
							for (int j = 0; j < n; j++)
							{
								pt = T[e][j] * E[j][f];
								ww += pt;
							}
							Q[e][f] = ww;
							ww = 0;
							pt = 1;
						}
					}

					//Перезапись полученной ортогональной матрицы
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							E[e][f] = Q[e][f];
						}
					}

					//Перезапись полученной матрицы AtA
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							R[e][f] = R1[e][f];
						}
					}
					k++;
				}
			}

			//Перезапись полученной ортогональной матрицы
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					Q[j][i] = E[i][j];
				}
			}

		    //Получение измененной матрицы AtA путем перемножения матрицы R на матрицу Q   
			for (int e = 0; e < n; e++)
			{
				for (int f = 0; f < n; f++)
				{
					for (int j = 0; j < n; j++)
					{
						pt = R[e][j] * Q[j][f];
						ww += pt;
					}
					R1[e][f] = ww;
					ww = 0;
					pt = 1;	
				}
			}

			//Перезапись полученной матрицы 
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					R[i][j] = R1[i][j];
				}
			}

			//Устранение предельно малых чисел для более точных подсчетов
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
						R[i][j] = 0;
				}
			}

			//Проверка состояния матрицы с собственными числами на главной диагонали
			vs = 0;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (i != j)
					{
						if (R[i][j] != 0)
							vs++;
					}
				}
			}
		}
		cout << endl;

		//Вывод искомой диагональной матрицы с собственными числами в невозрастающем по модулю порядке
		cout << " Matrix AtA Diagonal" << endl;
		for (int e = 0; e < n; e++)
		{
			for (int f = 0; f < n; f++)
			{
				cout << setw(10) << R[e][f] << "\t";
			}
			cout << endl;
		}

		//Запись собственных чисел в отдельных массив для дальнейшего пользования
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					 L[i] = R[i][j];
			}
		}

		//Нахождение собственных векторов исходной матрицы АtA в соответствии с ее собственными числами
		for (int t = 0; t < n; t++)
		{
			//Перезапись исходной матрицы в отдельный массив
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					R[i][j] = AtA[i][j];
				}
			}

			//Приводим матрицу AtA к форме AtA - L*E, где - собственное число матрицы AtA, E - единичная матрица 
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (i == j)
					{
						R[i][j] -= L[t];
					}
				}
			}

			//Приведение полученной матрицы к верхней диагональной методом Гаусса
			double f;
			for (int l = 0; l < n - 1; l++)
			{
					if (R[l][l] != 0)
					{
						for (int i = l; i < n - 1; i++)
						{
							f = R[i + 1][l] / R[l][l];
							for (int j = l; j < n; j++)
							{
								R[i + 1][j] -= R[l][j] * f;
							}
						}
					}	
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}
			if (n > 3)
				R[n - 1][n - 1] = 0;

			//Приведение полученной матрицы к диагональной обратным методом Гаусса
			for (int l = n - 1; l >= 1; l--)
			{
				if (R[l][l] != 0)
				{
					for (int i = l; i >= 1; i--)
					{
						f = R[i - 1][l] / R[l][l];
						for (int j = n-1; j >= 0; j--)
						{
							R[i - 1][j] -= R[l][j] * f;
						}
					}
				}
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}

			//Приведение диагональных чисел матрицы к единичным значениям
			double s;
			for (int l = 0; l < n; l++)
			{
				if (R[l][l] != 0)
				{
					s = 1 / R[l][l];
					for (int j = l; j < n; j++)
						R[l][j] *= s;
				}
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}

			//Нахождение номера столбца, содержащего координаты собственного вектора
			int lt;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (R[i][j] == 0)
						lt = j;
				}
			}

			//Заполнение ортогональной матрицы V собственными векторами
			double ss = 0;
			for (int i = n - 1; i >= 0; i--)
			{
				for (int j = 0; j < n; j++)
					ss += R[i][j];
				if (R[i][i] == abs(ss))
					U[i][t] = 0;
				if ((ss == 0) && (R[i][i] != 1))
					U[i][t] = 1;
				if ((abs(ss) != 1) && (abs(ss) != 0))
					U[i][t] = -R[i][lt];
				ss = 0;
			}
		}

		//Перезапись данных в дополнительный массив, параллельно транспанируя матрицу
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				R[j][i] = U[i][j];
			}
		}

        //Нормирование векторов в матрице V 
		double nor;
		for (int i = 0; i < n; i++)
		{
			s = 0;
			for (int j = 0; j < n; j++)
			{
				s += square(R[i][j]);
			}
			nor = sqrt(s);
			for (int j = 0; j < n; j++)
			{
				R[i][j] /= nor;
			}

		}
		
		//Перезапись данных в дополнительную матрицу
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				AtA[i][j] = R[i][j];
			}
		}

		//Вычисление промежуточной матрицы C путем перемножения исходной матрицы А на V транспанированную ненормированную
		s = 0;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				for (int l = 0; l < n; l++)
				{
					p = A[i][l] * U[l][j];
					s += p;
				}
				R1[i][j] = s;
				s = 0;
			}
		}

		//Устранение погрешностей 
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
						if (abs(R1[i][j]) < 0.0001)
						{
							R1[i][j] = 0;
						}
			}
		}

		//Перезапись данных в дополнительную транспанированную матрицу
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				R[j][i] = R1[i][j];
			}
		}

		//Приведение полученной матрицы к диагональной прямым методом Гаусса
		double f;
		for (int l = 0; l < n - 1; l++)
		{
			if (R[l][l] != 0)
			{
				for (int i = l; i < n - 1; i++)
				{
					f = R[i + 1][l] / R[l][l];
					for (int j = l; j < n; j++)
					{
						R[i + 1][j] -= R[l][j] * f;
					}
				}
			}
		}

		//Устранение погрешностей
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (abs(R[i][j]) < 0.0001)
				{
					R[i][j] = 0;
				}
				if (abs(R[i][j]) == 0)
				{
					R[i][j] = abs(R[i][j]);
				}
			}
		}

		//Приведение диагональных чисел матрицы к единичным значениям
		for (int l = 0; l < n; l++)
		{
			if (R[l][l] != 0)
			{
				s = 1 / R[l][l];
				for (int j = l; j < m; j++)
					R[l][j] *= s;
			}
		}

		//Составление дополнительных ортогональных векторов для матрицы Q
		if (m > n)
		{
			s = 0;
			int t, tt = 0;
			for (int i = 0; i < m - n; i++)
			{
				for (t = m - 1; t >= n; t--)
				{
					X[t] = 1 + rand() % 5;
					tt++;
				}

				for (int j = n - 1; j >= 0; j--)
				{
					for (int k = m - 1; k > j; k--)
					{
						s += R[j][k] * X[k];
					}
					X[m - 1 - tt] = -s;
					s = 0;
					tt++;
				}
				tt = 0;
				for (int e = 0; e < m; e++)
				{
					At[e][i] = X[e];
					E[e][i] = X[e];
				}
			}

			//Применение ортогонализации Грамма-Шмидта для векторов, входящих в ортогональное дополнение
			double s1 = 0, s2 = 0, p1;
			if (m - n > 1)
			{
				for (int i = 1; i < m - n; i++)
				{
					for (int k = i; k > 0; k--)
					{
						t = k - 1;
						for (int j = 0; j < m; j++)
						{
							p1 = At[j][i] * E[j][t];
							s1 += p1;
							p1 = square(E[j][t]);
							s2 += p1;
						}
						for (int j = 0; j < m; j++)
						{
							E[j][i] -= (s1 / s2)*E[j][t];
						}
						s1 = 0;
						s2 = 0;
					}
				}
			}
		}

		//Добавление полученных ортогональных векторов в матрицу Q
		for (int i = 0; i < m - n; i++)
		{
			for (int j = 0; j < m; j++)
			{
				R1[j][n + i] = E[j][i];
			}
		}

		//Нормирование векторов матрицы Q
		for (int j = 0; j < m; j++)
		{
			s = 0;
			for (int i = 0; i < m; i++)
			{
				s += square(R1[i][j]);
			}
			nor = sqrt(s);
			for (int i = 0; i < m; i++)
			{
				R1[i][j] /= nor;
			}
		}

		//Вывод искомого сингулярного разложения матрицы
		cout << endl;
		cout << " Singular Value Decomposition" << endl;

		cout << endl;
		cout << " Matrix U" << endl;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cout << setw(5) << setprecision(2) << R1[i][j] << "\t";
			}
			cout << endl;
		}

		cout << endl;
		cout << " Matrix S" << endl;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					T[i][j] = sqrt(L[i]);
				else
					T[i][j] = 0;
				cout << setw(4) << setprecision(2) << T[i][j] << "\t";
			}
			cout << endl;
		}

		cout << endl;
		cout << " Matrix Vt" << endl;
		cout << endl;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << setw(4) << setprecision(2) << AtA[i][j] << "\t";
			}
			cout << endl;
		}
		cout << endl;

	}
	else
	{
		//Перемножение матрицы А на транспанированную матрицу А
		cout << " Matrix A*At\n";
		cout << endl;
		double s = 0;
		int k = 0;
		double p = 1;
		for (int i = 0; i < n; i++)
		{
			for (int l = 0; l < n; l++)
			{
				for (int j = 0; j < m; j++)
				{
					p = At[i][j] * A[j][l];
					s += p;
				}
				AtA[i][l] = s;
				s = 0;
			}
		}

		//Выводим  Матрицу AtA
		cout << endl;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << AtA[i][j] << "\t";
			}
			cout << endl;
		}

		//Перенос данных матрицы AtA в дополнительную
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				R[i][j] = AtA[i][j];
			}
		}

		//Нахождение собственных чисел матрицы через QR - разложение  
		int vs = 1; //Сумма элементов, не лежащих на главной диагонали
		double cos, sin; //cos - косинус угла поворота; sin - синус угла поворота
		int k1 = 0;
		double ww = 0;
		double pt = 1;

		//Цикл для вывода собственных чисел матрицы на её главной диагонали
		while (vs != 0)
		//for (int ii = 0; ii < 3; ii++)
		{

			//Создание единичной матрицы (начальный вид ортогональной матрицы)
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (i == j)
						E[i][j] = 1;
					else
						E[i][j] = 0;
				}
			}

			//Получение QR-разложения для матрицы AtA
			for (int l = 0; l < n - 1; l++)
			{
				for (int i = l + 1; i < n; i++)
				{
					//cout << endl;
					//cout << "Matrix Rotation " << k1 + 1 << endl;
					//cout << endl;
					cos = R[l][l] / sqrt(square(R[l][l]) + square(R[i][l]));  //Значение косинуса
					sin = R[i][l] / sqrt(square(R[l][l]) + square(R[i][l]));  //Значение синуса

					//Составляем матрицу вращений Гивенса T для матрицы AtA 
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							if (((e == f) && (e == l)) || ((e == f) && (e == i)))
								T[e][f] = cos;
							else
								if ((e != f) && (e == i) && (f == l))
									T[e][f] = -sin;
								else
									if ((e != f) && (e == l) && (f == i))
										T[e][f] = sin;
									else
										if (e == f)
											T[e][f] = 1;
										else
											if (e != f)
												T[e][f] = 0;
							//cout << setw(10) << T[e][f] << "\t";
						}
						//cout << endl;
					}

					//Постепенное обнуление столбцов под главной изменяемой матрицы AtA 
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{

							//Перемножение матрицы вращений на изменяемую матрицу AtA
							for (int j = 0; j < n; j++)
							{
								pt = T[e][j] * R[j][f];
								ww += pt;
							}
							R1[e][f] = ww;
							ww = 0;
							pt = 1;

							//Составление ортогональной матрицы путем перемножения полученной матрицы вращения на предыдущую
							for (int j = 0; j < n; j++)
							{
								pt = T[e][j] * E[j][f];
								ww += pt;
							}
							Q[e][f] = ww;
							ww = 0;
							pt = 1;
						}
					}

					//Перезапись полученной ортогональной матрицы
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							E[e][f] = Q[e][f];
						}
					}

					//Перезапись полученной матрицы AtA
					for (int e = 0; e < n; e++)
					{
						for (int f = 0; f < n; f++)
						{
							R[e][f] = R1[e][f];
						}
					}
					k1++;
				}
			}

			//Перезапись полученной ортогональной матрицы
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					Q[j][i] = E[i][j];
				}
			}

			//Получение измененной матрицы AtA путем перемножения матрицы R на матрицу Q   
			for (int e = 0; e < n; e++)
			{
				for (int f = 0; f < n; f++)
				{
					for (int j = 0; j < n; j++)
					{
						pt = R[e][j] * Q[j][f];
						ww += pt;
					}
					R1[e][f] = ww;
					ww = 0;
					pt = 1;
				}
			}

			//Перезапись полученной матрицы 
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					R[i][j] = R1[i][j];
				}
			}

			//Устранение предельно малых чисел для более точных подсчетов
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
						R[i][j] = 0;
				}
			}

			//Проверка состояния матрицы с собственными числами на главной диагонали
			vs = 0;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (i != j)
					{
						if (R[i][j] != 0)
							vs++;
					}
				}
			}

			//cout << "Evgeniy gey!" << endl;
		}
		cout << endl;

		//Вывод искомой диагональной матрицы с собственными числами в невозрастающем по модулю порядке
		cout << " Matrix AtA Diagonal" << endl;
		for (int e = 0; e < n; e++)
		{
			for (int f = 0; f < n; f++)
			{
				cout << setw(10) << R[e][f] << "\t";
			}
			cout << endl;
		}

		//Запись собственных чисел в отдельных массив для дальнейшего пользования
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					L[i] = R[i][j];
			}
		}

		//Нахождение собственных векторов исходной матрицы АtA в соответствии с ее собственными числами
		for (int t = 0; t < n; t++)
		{
			//Перезапись исходной матрицы в отдельный массив
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					R[i][j] = AtA[i][j];
				}
			}

			//Приводим матрицу AtA к форме AtA - L*E, где - собственное число матрицы AtA, E - единичная матрица 
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (i == j)
					{
						R[i][j] -= L[t];
					}
				}
			}

			//Приведение полученной матрицы к верхней диагональной методом Гаусса
			double f;
			for (int l = 0; l < n - 1; l++)
			{
				if (R[l][l] != 0)
				{
					for (int i = l; i < n - 1; i++)
					{
						f = R[i + 1][l] / R[l][l];
						for (int j = l; j < n; j++)
						{
							R[i + 1][j] -= R[l][j] * f;
						}
					}
				}
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}
			if (n > 3)
				R[n - 1][n - 1] = 0;

			//Приведение полученной матрицы к диагональной обратным методом Гаусса
			for (int l = n - 1; l >= 1; l--)
			{
				if (R[l][l] != 0)
				{
					for (int i = l; i >= 1; i--)
					{
						f = R[i - 1][l] / R[l][l];
						for (int j = n - 1; j >= 0; j--)
						{
							R[i - 1][j] -= R[l][j] * f;
						}
					}
				}
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}

			//Приведение диагональных чисел матрицы к единичным значениям
			double s;
			for (int l = 0; l < n; l++)
			{
				if (R[l][l] != 0)
				{
					s = 1 / R[l][l];
					for (int j = l; j < n; j++)
						R[l][j] *= s;
				}
			}

			//Устранение вычислительных погрешностей
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (abs(R[i][j]) < 0.0001)
					{
						R[i][j] = 0;
					}
					if (abs(R[i][j]) == 0)
					{
						R[i][j] = abs(R[i][j]);
					}
				}
			}

			//Нахождение номера столбца, содержащего координаты собственного вектора
			int lt;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < n; j++)
				{
					if (R[i][j] == 0)
						lt = j;
				}
			}

			//Заполнение ортогональной матрицы V собственными векторами
			double ss = 0;
			for (int i = n - 1; i >= 0; i--)
			{
				for (int j = 0; j < n; j++)
					ss += R[i][j];
				if (R[i][i] == abs(ss))
					U[i][t] = 0;
				if ((ss == 0) && (R[i][i] != 1))
					U[i][t] = 1;
				if ((abs(ss) != 1) && (abs(ss) != 0))
					U[i][t] = -R[i][lt];
				ss = 0;
			}
		}

		//Перезапись данных в дополнительный массив, параллельно транспанируя матрицу
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				R[j][i] = U[i][j];
			}
		}

		//Нормирование векторов в матрице V 
		double nor;
		for (int i = 0; i < n; i++)
		{
			s = 0;
			for (int j = 0; j < n; j++)
			{
				s += square(R[i][j]);
			}
			nor = sqrt(s);
			for (int j = 0; j < n; j++)
			{
				R[i][j] /= nor;
			}

		}

		//Перезапись данных в дополнительную матрицу
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				AtA[i][j] = R[i][j];
			}
		}

		//Вычисление промежуточной матрицы C путем перемножения исходной матрицы А на V транспанированную ненормированную
		s = 0;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				for (int l = 0; l < n; l++)
				{
					p = A[i][l] * U[l][j];
					s += p;
				}
				R1[i][j] = s;
				s = 0;
			}
		}

		//Перезапись данных в дополнительную матрицу
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < m; j++)
			{
				R[i][j] = R1[i][j];
			}
		}

		//Перезапись данных в дополнительную матрицу
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < m; j++)
			{
				R1[i][j] = R[i][j];
			}
		}

		//Нормирование векторов матрицы Q
		for (int j = 0; j < m; j++)
		{
			s = 0;
			for (int i = 0; i < m; i++)
			{
				s += square(R1[i][j]);
			}
			nor = sqrt(s);
			for (int i = 0; i < m; i++)
			{
				R1[i][j] /= nor;
			}
		}

		//Вывод искомого сингулярного разложения матрицы
		cout << endl;
		cout << " Singular Value Decomposition" << endl;

		cout << endl;
		cout << " Matrix U" << endl;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < m; j++)
			{
				cout << setw(5) << setprecision(2) << R1[i][j] << "\t";
			}
			cout << endl;
		}

		cout << endl;
		cout << " Matrix S" << endl;
		cout << endl;
		for (int i = 0; i < m; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (i == j)
					T[i][j] = sqrt(L[i]);
				else
					T[i][j] = 0;
				cout << setw(4) << setprecision(2) << T[i][j] << "\t";
			}
			cout << endl;
		}

		cout << endl;
		cout << " Matrix Vt" << endl;
		cout << endl;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				cout << setw(4) << setprecision(2) << AtA[i][j] << "\t";
			}
			cout << endl;
		}
		cout << endl;

	}
	cout << endl;
	cout << "Ohh you tuch my tra-la-la.." << endl;
	cout << "Ohh my din-din-don.." << endl;
	system("pause");
	return 0;
}
// Запуск программы: CTRL+F5 или меню "Отладка" > "Запуск без отладки"
// Отладка программы: F5 или меню "Отладка" > "Запустить отладку"

// Советы по началу работы 
//   1. В окне обозревателя решений можно добавлять файлы и управлять ими.
//   2. В окне Team Explorer можно подключиться к системе управления версиями.
//   3. В окне "Выходные данные" можно просматривать выходные данные сборки и другие сообщения.
//   4. В окне "Список ошибок" можно просматривать ошибки.
//   5. Последовательно выберите пункты меню "Проект" > "Добавить новый элемент", чтобы создать файлы кода, или "Проект" > "Добавить существующий элемент", чтобы добавить в проект существующие файлы кода.
//   6. Чтобы снова открыть этот проект позже, выберите пункты меню "Файл" > "Открыть" > "Проект" и выберите SLN-файл.
