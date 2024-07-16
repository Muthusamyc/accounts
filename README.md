public async Task<CommonRsult> InsertSupportTeam(SPSupportTeamTable supportteam)
{
    CommonRsult result = new CommonRsult();
    try
    {

        DataTable dt = new DataTable();
        var con = (SqlConnection)_context.Database.GetDbConnection();
        using (var cmd = new SqlCommand("IT.sp_SupportTeam", con))
        {
            cmd.CommandType = CommandType.StoredProcedure;
            cmd.Parameters.AddWithValue("@Flag", supportteam.Flag);
            cmd.Parameters.AddWithValue("@SupportTeamID", supportteam.SupportTeamId);
            cmd.Parameters.AddWithValue("@SupportTeamAssgnID", supportteam.SupportTeamAssgnID);
            cmd.Parameters.AddWithValue("@Email", supportteam.Email);
            cmd.Parameters.AddWithValue("@First_Name", supportteam.FirstName);
            cmd.Parameters.AddWithValue("@Middle_Name", supportteam.MiddleName);
            cmd.Parameters.AddWithValue("@Last_Name", supportteam.LastName);
            cmd.Parameters.AddWithValue("@Img_Url", supportteam.ImgUrl);
            cmd.Parameters.AddWithValue("@Designation", supportteam.Designation);
            cmd.Parameters.AddWithValue("@Role", supportteam.Role);
            cmd.Parameters.AddWithValue("@EmpID", supportteam.EmpId);
            cmd.Parameters.AddWithValue("@IsActive", supportteam.IsActive);
            cmd.Parameters.AddWithValue("@DOL", supportteam.Dol);
            cmd.Parameters.AddWithValue("@DOB", supportteam.Dob);
            cmd.Parameters.AddWithValue("@IsAdmin", supportteam.IsAdmin);
            cmd.Parameters.AddWithValue("@isSuperAdmin", supportteam.isSuperAdmin);
            cmd.Parameters.AddWithValue("@IsApprover", supportteam.IsApprover);
            cmd.Parameters.AddWithValue("@IsChangeAnalyst", supportteam.IsChangeAnalyst);
            cmd.Parameters.AddWithValue("@IsSupportEngineer", supportteam.IsSupportEngineer);
            cmd.Parameters.AddWithValue("@PlantID", supportteam.PlantId);
            cmd.Parameters.AddWithValue("@SupportID", supportteam.SupportId);
            cmd.Parameters.AddWithValue("@CategoryID", supportteam.CategoryId);
            cmd.Parameters.AddWithValue("@CategoryTypID", supportteam.CategoryTypID);
            cmd.Parameters.AddWithValue("@ClassificationID", supportteam.ClassificationId);
            cmd.Parameters.AddWithValue("@ApproverstageCR", supportteam.ApproverstageCR);
            cmd.Parameters.AddWithValue("@ApproverstageR", supportteam.ApproverstageR);
            cmd.Parameters.AddWithValue("@ApproverstageC", supportteam.ApproverstageC);
            cmd.Parameters.AddWithValue("@Level", supportteam.Level);
            cmd.Parameters.AddWithValue("@Approverstage2CR", supportteam.Approverstage2CR);
            cmd.Parameters.AddWithValue("@Approverstage2R", supportteam.Approverstage2R);
            cmd.Parameters.AddWithValue("@Approverstage2C", supportteam.Approverstage2C);
            cmd.Parameters.AddWithValue("@Level2", supportteam.Level2);
            cmd.Parameters.AddWithValue("@Approverstage3CR", supportteam.Approverstage3CR);
            cmd.Parameters.AddWithValue("@Approverstage3R", supportteam.Approverstage3R);
            cmd.Parameters.AddWithValue("@Approverstage3C", supportteam.Approverstage3C);
            cmd.Parameters.AddWithValue("@Level3", supportteam.Level3);
            cmd.Parameters.AddWithValue("@CreatedBy", supportteam.CreatedBy);

            using (var da = new SqlDataAdapter(cmd))
            {
                await Task.Run(() => da.Fill(dt));
                result.Type = "S";
                result.Message = "Insert Successfully";

            }
        }
    }
    catch (Exception)
    {
        result.Type = "E";
        result.Message = "Insert failed";
    }
    return result;
}

above my reposity and below my Models


public class SPSupportTeamTable
{
    public string Flag { get; set; }

    public int SupportTeamId { get; set; }

    public int SupportTeamAssgnID { get; set; }

    public string? Email { get; set; }

    public string? FirstName { get; set; }

    public string? MiddleName { get; set; }

    public string? LastName { get; set; }

    public string? ImgUrl { get; set; }

    public string? Designation { get; set; }

    public string? Role { get; set; }

    public int? EmpId { get; set; }

    public bool? IsActive { get; set; }

    public string? Dol { get; set; }

    public string? Dob { get; set; }

    public bool? IsAdmin { get; set; }

    public bool? isSuperAdmin { get; set; }

    public bool? IsApprover { get; set; }

    public bool? IsChangeAnalyst { get; set; }

    public bool? IsSupportEngineer { get; set; }

    public int? PlantId { get; set; }

    public int SupportId { get; set; }

    public int? CategoryId { get; set; }
    public int? CategoryTypID { get; set; }

    public int? ClassificationId { get; set; }

    public string? ApproverstageCR { get; set; }

    public string? ApproverstageR { get; set; }

    public string? ApproverstageC { get; set; }

    public int? Level { get; set; }

    public string? Approverstage2CR { get; set; }

    public string? Approverstage2R { get; set; }

    public string? Approverstage2C { get; set; }

    public int? Level2 { get; set; }

    public string? Approverstage3CR { get; set; }

    public string? Approverstage3R { get; set; }

    public string? Approverstage3C { get; set; }

    public int? Level3 { get; set; }



    public int? CreatedBy { get; set; }

    public DateTime? CreatedDate { get; set; }
}

and this is my giving request
{
  "flag": "I",
  "supportTeamId": 0,
  "supportTeamAssgnID": 0,
  "email": "string",
  "firstName": "Shyam",
  "middleName": "Kumar",
  "lastName": "Sharma",
  "imgUrl": "string",
  "designation": "string",
  "role": "Change Analyst,Executive",
  "empId": 107355,
  "isActive": true,
  "dol": "string",
  "dob": "string",
  "isAdmin": true,
  "isSuperAdmin": false,
  "isApprover": false,
  "isChangeAnalyst": true,
  "isSupportEngineer": true,
  "plantId": 5,
  "supportId": 1,
  "categoryId": 1,
  "categoryTypID": 0,
  "classificationId": 0,
  "approverstageCR": "string",
  "approverstageR": "string",
  "approverstageC": "string",
  "level": 0,
  "approverstage2CR": "string",
  "approverstage2R": "string",
  "approverstage2C": "string",
  "level2": 0,
  "approverstage3CR": "string",
  "approverstage3R": "string",
  "approverstage3C": "string",
  "level3": 0,
  "createdBy": 1,
  "createdDate": "2024-07-16T12:19:25.430Z"
}
