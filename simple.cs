class Author {
    public string Name { get; set; }
    public string TwitterHandle { get; set;}
    public string Company { get; set;}

    static public IEnumerable<String> TwitterHandles(IEnumerable<Author> authors, string company) {
        var result = new List<String> ();
        var loopStart = authors
            .Where(a => a.Company == company)
            .Select(a => a.TwitterHandle); /***/
        foreach (string handle in loopStart) {
            if (handle != null)
                result.Add(handle);
        }
        return result;
    }
}