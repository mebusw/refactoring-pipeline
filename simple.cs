class Author {
    public string Name { get; set; }
    public string TwitterHandle { get; set;}
    public string Company { get; set;}

    static public IEnumerable<String> TwitterHandles(IEnumerable<Author> authors, string company) {
        var result = new List<String> ();
        var loopStart = authors
            .Where(a => a.Company == company); /***/
        foreach (Author a in loopStart) {
                var handle = a.TwitterHandle;
                if (handle != null)
                    result.Add(handle);
        }
        return result;
    }
}