private readonly ILogger<YourController> _logger;

public YourController(ILogger<YourController> logger)
{
    _logger = logger;
}

public async Task<IActionResult> GetEmployee(int pagesize = 10)
{
    try
    {
        // Your existing code here

        _logger.LogInformation("GetEmployee method executed successfully.");
        return Ok(allData);
    }
    catch (Exception ex)
    {
        _logger.LogError($"An error occurred in GetEmployee method: {ex.Message}");
        return StatusCode(StatusCodes.Status500InternalServerError, $"Internal server error: {ex.Message}");
    }
}











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
