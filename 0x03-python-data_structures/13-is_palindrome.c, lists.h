#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current;
	int i = 0, copied_list[4000];

	current = *head;
	while (current)
	{
		copied_list[i] = current->n;
		i += 1;
		current = current->next;
	}
	current = *head;
	i -= 1;
	while (current)
	{
		if (current->n == copied_list[i])
		{
			i -= 1;
			current = current->next;
		}
		else
			return (0);
	}
	return (1);
}