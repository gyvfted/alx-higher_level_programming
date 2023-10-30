#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *lts = list;
	listint_t *aux = lts;

	while (lts && aux && lts->next)
	{
		aux = aux->next;
		lts = lts->next->next;
		if (aux == lts)
			return (1);
	}
	return (0);
}
