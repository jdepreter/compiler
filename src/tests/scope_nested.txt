int main(){{
    int c = 1;
    {
        int c = 1;
        c = c + 1;
        printf(c);
    }
    c = c + 2;
    printf(c);
}
return 0;
}