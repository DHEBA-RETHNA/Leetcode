bool rotateString(char* s, char* goal) {
    if (strlen(s) != strlen(goal)) return false;
    char da[strlen(s) * 2 + 1];
    strcpy(da, s);
    strcat(da, s);
    if (strstr(da, goal) == NULL)
        return false;
    return true;
}