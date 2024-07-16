cmd.Parameters.AddWithValue("@DOL", string.IsNullOrEmpty(supportteam.Dol?.ToString()) ? (object)DBNull.Value : supportteam.Dol);
            cmd.Parameters.AddWithValue("@DOB", string.IsNullOrEmpty(supportteam.Dob?.ToString()) ? (object)DBNull.Value : supportteam.Dob);





 public DateTime? Dol { get; set; }
    public DateTime? Dob { get; set; }  // Updated to DateTime?
