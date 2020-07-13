import algorithms
import time
import os
import sys
import pygame

dimensions = [1024,1024]

algorithms = {"SelectionSort": algorithms.SelectionSort(), "BubbleSort": algorithms.BubbleSort(), "InsertionSort": algorithms.InsertionSort(), "MergeSort": algorithms.MergeSort(), "QuickSort": algorithms.QuickSort()}

if len(sys.argv) > 1:
    if sys.argv[1] == "list"
        for key in algorithms.key(): print(key, end=" ")
        print("")
        sys.exit(0)
    

pygame.init()
display = pygame.display.set_mode((dimensions[0], dimensions[1]))
display.fill(pygame.Color("#a48be0"))

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update(algorithms, swap1 = None, swap2 = None, display=display):
    display.fill(pygame.Color("#a48be0"))
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Sorting...".format(algorithm.name, time.time() - algorithm.start_time)) # Display title 
    k = int(dimensions[0]/len(algorithm.array))
    for i in range(len(algorithm.array)):
        color = (80, 0, 255)
        if swap1 == algorithm.array[i]:
            color = (0, 255, 0)
        elif swap2 == algorithm.array[i]:
            color = (255, 0, 0)
        
        pygame.draw.rect(display, color, (i*k,dimensions[1],k,-algorithm.array[i]))
    check_event()
    pygame.display.update()

def keep_open(algorithm, display, time): # Keep the window open until sort completion
    pygame.display.set_caption("Sorting Visualizer     Algorithm: {}     Time: {:.3f}      Status: Done!".format(algorithm.name, time))
    while True:
        check_events()
        pygame.display.update()

def main():
    if len(sys.argv) < 2:
        print("Please select a sorting algorithm.") 
    else:
        try:
            algorithm = algorithms[sys.argv[1]] # Pass the algorithm selected
            try:
                time_elapsed = algorithm.run()[1]
                keep_open(algorithm, display, time_elapsed)
                pass
            except:
                pass
        except:
            print("Error.")

if __name__ == "__main__":
    main()
