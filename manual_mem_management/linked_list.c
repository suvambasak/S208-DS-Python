#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int data;
    struct node *next;
} node;

node *HEAD = NULL;

int insert()
{
    char another_node;
    do
    {
        node *p = (node *)malloc(sizeof(node));
        p->next = NULL;

        printf("\nENTER DATA : ");
        scanf("%d", &p->data);

        if (HEAD == NULL)
        {
            HEAD = p;
            p = NULL;
        }
        else
        {
            node *temp = HEAD;

            while (temp->next != NULL)
                temp = temp->next;

            temp->next = p;
            p = NULL;
            temp = NULL;
        }

        printf("\nDO YOU WANT TO ENTER ANOTHER NODE? (Y/N) :: ");
        getchar();
        another_node = getchar();

    } while (another_node == 'Y' || another_node == 'y');

    return 1;
}

int display()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return -1;
    }
    else
    {
        node *temp = HEAD;

        printf("\nDISPLAY :");
        while (temp->next != NULL)
        {
            printf(" %d -> ", temp->data);
            temp = temp->next;
        }
        printf(" %d -> NULL\n\n", temp->data);
        temp = NULL;
        return 1;
    }
}

int insert_at_first()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return insert();
    }
    else
    {
        node *p = (node *)malloc(sizeof(node));

        printf("\nENTER DATA : ");
        scanf("%d", &p->data);
        p->next = HEAD;
        HEAD = p;
        p = NULL;

        return 1;
    }
}

int insert_at_last()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return insert();
    }
    else
    {
        node *p = (node *)malloc(sizeof(node));
        p->next = NULL;
        printf("\nENTER DATA : ");
        scanf("%d", &p->data);

        node *temp = HEAD;
        while (temp->next != NULL)
            temp = temp->next;

        temp->next = p;

        p = NULL;
        temp = NULL;

        return 1;
    }
}

int insert_at_intermediate()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return insert();
    }
    else
    {
        int position;
        printf("\nENTER POSITION : ");
        scanf("%d", &position);
        if (position == 1)
        {
            return insert_at_first();
        }
        node *p = (node *)malloc(sizeof(node));
        p->next = NULL;
        printf("\nENTER DATA : ");
        scanf("%d", &p->data);

        node *temp = HEAD;

        while (temp->next != NULL && position-- > 2)
        {
            temp = temp->next;
        }

        p->next = temp->next;
        temp->next = p;

        p = NULL;
        temp = NULL;

        return 1;
    }
}

int delete_first()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return -1;
    }
    else
    {
        node *del = HEAD;
        HEAD = HEAD->next;

        del->next = NULL;
        free(del);

        return 1;
    }
}

int delete_last()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return -1;
    }
    else
    {
        node *temp = HEAD;

        while (temp->next->next != NULL)
            temp = temp->next;

        node *del = temp->next;
        temp->next = NULL;
        temp = NULL;

        free(del);
        del = NULL;
        return 1;
    }
}

int delete_from_intermediate()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return -1;
    }
    else
    {
        int position;
        printf("\nENTER POSITION : ");
        scanf("%d", &position);
        if (position == 1)
        {
            return delete_first();
        }

        node *temp = HEAD;
        while (temp->next != NULL && position-- > 2)
        {
            temp = temp->next;
        }

        node *del = temp->next;

        temp->next = temp->next->next;
        del->next = NULL;

        free(del);
        del = NULL;

        return 1;
    }
}

int reverse()
{
    if (HEAD == NULL)
    {
        printf("\n\tLIST IS EMPTY!!");
        return -1;
    }
    else
    {
        node *p = NULL, *q = NULL, *r = HEAD;

        while (r)
        {
            p = r->next;
            r->next = q;
            q = r;
            r = p;
        }

        HEAD = q;

        return display();
    }
}

void main()
{
    int choice, control;
    control = 1;
    while (control)
    {

        printf("\n<<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>");
        printf("\n1-> INSERT");
        printf("\n2-> DISPLAY");
        printf("\n3-> INSERT AT FIRST POSITION");
        printf("\n4-> INSERT AT LAST POSITION");
        printf("\n5-> INSERT AT INTERMEDIATE POSITION");
        printf("\n6-> DELETE FIRST");
        printf("\n7-> DELETE LAST");
        printf("\n8-> DELETE FROM INTERMEDIATE POSITION");
        printf("\n9-> REVERSE OF THE LIST");

        printf("\n\n0-> EXIT\n");
        printf("---------------------------------------");

        printf("\nENTER CHOICE : ");
        scanf("%d", &choice);

        switch (choice)
        {
        case 0:
            exit(1);
        case 1:
            insert();
            break;
        case 2:
            display();
            break;
        case 3:
            insert_at_first();
            break;
        case 4:
            insert_at_last();
            break;
        case 5:
            insert_at_intermediate();
            break;
        case 6:
            delete_first();
            break;
        case 7:
            delete_last();
            break;
        case 8:
            delete_from_intermediate();
            break;
        case 9:
            reverse();
            break;
        default:
            printf("\n INVALID INPUT!");
        }
    }
}

// (base) suvam@KD-304G:/mnt/Storage/Repositories/S208-DS-Python/manual_mem_management$ cc linked_list.c && ./a.out

// <<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>
// 1-> INSERT
// 2-> DISPLAY
// 3-> INSERT AT FIRST POSITION
// 4-> INSERT AT LAST POSITION
// 5-> INSERT AT INTERMEDIATE POSITION
// 6-> DELETE FIRST
// 7-> DELETE LAST
// 8-> DELETE FROM INTERMEDIATE POSITION
// 9-> REVERSE OF THE LIST

// 0-> EXIT
// ---------------------------------------
// ENTER CHOICE : 1

// ENTER DATA : 1

// DO YOU WANT TO ENTER ANOTHER NODE? (Y/N) :: y

// ENTER DATA : 2

// DO YOU WANT TO ENTER ANOTHER NODE? (Y/N) :: y

// ENTER DATA : 3

// DO YOU WANT TO ENTER ANOTHER NODE? (Y/N) :: n

// <<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>
// 1-> INSERT
// 2-> DISPLAY
// 3-> INSERT AT FIRST POSITION
// 4-> INSERT AT LAST POSITION
// 5-> INSERT AT INTERMEDIATE POSITION
// 6-> DELETE FIRST
// 7-> DELETE LAST
// 8-> DELETE FROM INTERMEDIATE POSITION
// 9-> REVERSE OF THE LIST

// 0-> EXIT
// ---------------------------------------
// ENTER CHOICE : 2

// DISPLAY : 1 ->  2 ->  3 -> NULL

// <<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>
// 1-> INSERT
// 2-> DISPLAY
// 3-> INSERT AT FIRST POSITION
// 4-> INSERT AT LAST POSITION
// 5-> INSERT AT INTERMEDIATE POSITION
// 6-> DELETE FIRST
// 7-> DELETE LAST
// 8-> DELETE FROM INTERMEDIATE POSITION
// 9-> REVERSE OF THE LIST

// 0-> EXIT
// ---------------------------------------
// ENTER CHOICE : 6

// <<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>
// 1-> INSERT
// 2-> DISPLAY
// 3-> INSERT AT FIRST POSITION
// 4-> INSERT AT LAST POSITION
// 5-> INSERT AT INTERMEDIATE POSITION
// 6-> DELETE FIRST
// 7-> DELETE LAST
// 8-> DELETE FROM INTERMEDIATE POSITION
// 9-> REVERSE OF THE LIST

// 0-> EXIT
// ---------------------------------------
// ENTER CHOICE : 2

// DISPLAY : 2 ->  3 -> NULL

// <<<<<<<<<<<<<<< OPTIONS >>>>>>>>>>>>>>>>
// 1-> INSERT
// 2-> DISPLAY
// 3-> INSERT AT FIRST POSITION
// 4-> INSERT AT LAST POSITION
// 5-> INSERT AT INTERMEDIATE POSITION
// 6-> DELETE FIRST
// 7-> DELETE LAST
// 8-> DELETE FROM INTERMEDIATE POSITION
// 9-> REVERSE OF THE LIST

// 0-> EXIT
// ---------------------------------------
// ENTER CHOICE : 0