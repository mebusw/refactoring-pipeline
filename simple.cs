class Author {
    public string Name { get; set; }
    public string TwitterHandle { get; set;}
    public string Company { get; set;}

    static public IEnumerable<String> TwitterHandles(IEnumerable<Author> authors, string company) {
        var loopStart = authors
            .Where(a => a.Company == company)
            .Select(a => a.TwitterHandle)
            .Where (h => h != null); /***/
    }
}