#include "lists.h"

/**
 * insert_node - function that inserts a node to a list
 * @head: head of list
 * @number: number of the node
 * Return: the address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!current)
	{
		*head = new;
		free(new);
		return (new);
	}

	if (new->n < current->next->n)
	{
		new->next = current;
		current = new;
		return(new);
	}

	while (current->next && new->n > current->next->n)
		current = current->next;

	new->next = current->next;
	current->next = new;

	return (new);
}
