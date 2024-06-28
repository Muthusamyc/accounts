[HttpGet]
public async Task<IActionResult> GetEmployee()
{
    int pageno = 1; int pagesize = 10;
    int skip = (pageno - 1) * pagesize;
    int total = _context.VwEmployeeMasters.Count();
    
    for (int i = 0; i < total; i++)
    {
        var employeedata = await _context.VwEmployeeMasters
                        .OrderBy(c => c.EmployeeId)
                        .Skip(skip)
                        .Take(pagesize)
                        .ToListAsync();

        var count = employeedata.Count();
        return Ok(new { employeedata, count, skip, total });
    }
    return Ok(new { employeedata, count, skip, total });
}
