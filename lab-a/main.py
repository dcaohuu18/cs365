from uninformed_search import single_dfs, single_bfs
from greedy_bf_search import single_gbfs
from single_astar import single_astar
from multi_astar import multi_astar


def main():
	try:
		input_file = str(input('Please enter the input file name (for example, 1prize-open.txt): '))

		print('1. Depth-first\n2. Breadth-first\n3. Greedy-bf\n4. Single A*\n5. Multi A*')

		search_choice = int(input('Enter the according number to choose the desired search strategy: '))

		if search_choice == 1:
			single_dfs(input_file)

		elif search_choice == 2:
			single_bfs(input_file)

		elif search_choice == 3:
			single_gbfs(input_file)

		elif search_choice == 4:
			single_astar(input_file)

		elif search_choice == 5:
			multi_astar(input_file)

		else:
			raise ValueError 
	
	except FileNotFoundError:
		print("No file with such name!")

	except ValueError:
		print("Invalid number.") 


if __name__ == '__main__':
 	main() 