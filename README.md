public async Task<IActionResult> GetEmployee(int pagesize = 10)
{
    int pageno = 1; // Start from page 1
    int total = await _context.VwEmployeeMasters.CountAsync();

    List<object> allData = new List<object>();

    while ((pageno - 1) * pagesize < total)
    {
        int skip = (pageno - 1) * pagesize;

        var employeedata = await _context.VwEmployeeMasters
                                .OrderBy(c => c.EmployeeId)
                                .Skip(skip)
                                .Take(pagesize)
                                .ToListAsync();

        var count = employeedata.Count;

        var pageData = new { employeedata, count, skip, total };
        allData.Add(pageData);

        pageno++;
    }

    return Ok(allData);
}







[HttpGet]
public async Task<IActionResult> GetEmployees(int pageSize = 10)
{
    var result = await GetEmployee(pageSize);
    return result;
}
