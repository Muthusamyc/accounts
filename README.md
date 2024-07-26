 updateEndDateMin() {
   const fromDate = new Date(this.Value.downTimeFromDate);
   fromDate.setMinutes(fromDate.getMinutes() + 30);
   this.Value.downTimeToDate = fromDate.toISOString().slice(0, 16);
 }

 validateEndDate() {
   this.updateEndDateMin()
   const fromDate = new Date(this.Value.downTimeFromDate).getTime();
   const endDate = new Date(this.Value.downTimeToDate).getTime();

   if (endDate < fromDate + 30 * 60 * 1000) {
     alert("End Date and Time cannot be less than 30 minutes after the Start Date and Time.");
     this.Value.downTimeToDate = this.Value.downTimeToDate;
   }
 }
 above my ts and my html
 <div class="col" *ngIf="showRiskQ">
  <label>From Date <span style="color:red">*</span></label>
  <input type="datetime-local" [(ngModel)]="Value.downTimeFromDate" placeholder="" (change)="datetimefunction()" />
</div>
<div class="col" *ngIf="showRiskQ">
  <label>End Date <span style="color:red">*</span></label>
  <input type="datetime-local" [(ngModel)]="Value.downTimeToDate" placeholder="" [min]="minEndDate" (change)="validateEndDate()" />
</div>
