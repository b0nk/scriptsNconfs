#include <stddef.h>
#include <stdlib.h>
#include <string.h>
#include "hashmap.h"
 
typedef struct Node {
        struct Node *next;
        const char *key;
        void *data;
} Node;
 
HashMap *create_hashmap(size_t key_space) {
  HashMap *hm = (HashMap *)malloc(sizeof(HashMap));
  hm->size = key_space;
  hm->buckets = (Node **)calloc(1, sizeof(Node *) * key_space);

  return hm;
}
 
Node *create_node(const char *key, void *data, Node *previous, Node *next) {
  Node *new = (Node *)malloc(sizeof(Node));
  new->next = next;
  new->key = key;
  new->data = data;

  if (previous != 0) {
    previous->next = new;
  }
  return new;
}
 
unsigned int hash(const char *key) {
  unsigned int res = 0;
  for (int i = 0; key[i] != 0; i++) {
    res = res + key[i];
  }
  return res;
}
 
Node *lookup(HashMap *hm, const char *key, unsigned int index, Node **prev) {
  int setPrev = prev != 0;

  if (setPrev)
    *prev = 0;
  
  Node *curr = hm->buckets[index];
  while (curr != 0 && strcmp(key, curr->key) != 0 && curr->next != 0) {

    if (setPrev)
      *prev = curr;
    
    curr = curr->next;
  }
  return curr;
}
 
void insert_data(HashMap *hm, const char *key, void *data, ResolveCollisionCallback resolve_collision) {
  unsigned int index = hash(key) % hm->size;
  Node *curr = lookup(hm, key, index, 0);

  if (curr == 0)
    hm->buckets[index] = create_node(key, data, 0, 0);

  else if (strcmp(key, curr->key) == 0)
    curr->data = resolve_collision(curr->data, data);

  else if (curr->next == 0)
    curr->next = create_node(key, data, curr, 0);
  
}
 
void *get_data(HashMap *hm, const char *key) {
  unsigned int index = hash(key) % hm->size;
  Node *curr = lookup(hm, key, index, 0);

  if (curr != 0 && strcmp(key, curr->key) == 0)
    return curr->data;

  return NULL;
}
 
void iterate(HashMap *hm, void (*callback)(const char *key, void *data)) {
  for (unsigned int i = 0; i < hm->size; i++) {
    Node *curr = hm->buckets[i];

    if (curr != 0) {
      callback(curr->key, curr->data);

      while (curr->next != 0) {
        curr = curr->next;
        callback(curr->key, curr->data);
      }
    }
  }
}
 
void remove_data(HashMap *hm, const char *key, DestroyDataCallback destroy_data) {
  unsigned int index = hash(key) % hm->size;
  Node *previous;
  Node *curr = lookup(hm, key, index, &previous);

  if (curr != 0 && strcmp(key, curr->key) == 0) {

    if (previous != 0)
      previous->next = curr->next;

    else 
      hm->buckets[index] = 0;
    
    if (destroy_data != 0)
      destroy_data(curr->data);
    
    free(curr);
  }
}
 
void delete_node(Node *curr, DestroyDataCallback destroy_data) {
  if (curr->next != 0)
    delete_node(curr->next, destroy_data);
  
  if (destroy_data != 0)
    destroy_data(curr->data);
  
  free(curr);
}
 
void delete_hashmap(HashMap *hm, DestroyDataCallback destroy_data) {
  for (unsigned int i = 0; i < hm->size; i++) {
    Node *curr = hm->buckets[i];

    if (curr != 0)
      delete_node(curr, destroy_data);
    
  }
  free(hm->buckets);
  free(hm);
}
