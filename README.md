cmd.Parameters.AddWithValue("@DOL", supportteam.Dol.HasValue ? (object)supportteam.Dol.Value : DBNull.Value);
            cmd.Parameters.AddWithValue("@DOB", supportteam.Dob.HasValue ? (object)supportteam.Dob.Value : DBNull.Value);
