SELECT 
    CR.CRCODE,
    CR.Status,
    CR.[Stage],
    (SELECT concat(sta1.First_Name,'',sta1.Middle_Name,' ',sta1.Last_Name)
     FROM IT.CRApprover CRA 
	 left join  IT.SupportTeam sta1 on sta1.EmpID = CRA.ApproverID
     WHERE CRA.CRID = CR.ITCRID 
       AND CRA.ModifiedDt = (SELECT MAX(ModifiedDt) 
                             FROM IT.CRApprover 
                             WHERE CRID = CR.ITCRID)) AS LastApproverID,
