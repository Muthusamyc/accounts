select CR.CRCODE,CR.Status,CR.[Stage]
,(select Concat(CRA.ApproverID ,'-', CRA.ApprovedDt) LastApprBy from IT.CRApprover CRA where CRA.CRID=CR.ITCRID and ModifiedDt=(select max(ModifiedDt)  from IT.CRApprover where CRID=CR.ITCRID))

