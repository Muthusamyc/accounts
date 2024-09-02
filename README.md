SELECT 
    CR.CRCODE,
    CR.Status,
    CR.[Stage],
    (SELECT CRA.ApproverID 
     FROM IT.CRApprover CRA 
     WHERE CRA.CRID = CR.ITCRID 
       AND CRA.ModifiedDt = (SELECT MAX(ModifiedDt) 
                             FROM IT.CRApprover 
                             WHERE CRID = CR.ITCRID)) AS LastApproverID,
    (SELECT CRA.ApprovedDt 
     FROM IT.CRApprover CRA 
     WHERE CRA.CRID = CR.ITCRID 
       AND CRA.ModifiedDt = (SELECT MAX(ModifiedDt) 
                             FROM IT.CRApprover 
                             WHERE CRID = CR.ITCRID)) AS LastApprovedDate
FROM 
    IT.CR CR;
