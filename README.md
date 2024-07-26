<div class="col" *ngIf="showRiskQ">
  <label>From Date <span style="color:red">*</span></label>
  <input type="datetime-local" [(ngModel)]="downTimeFromDate" placeholder="" (change)="datetimefunction()" />
</div>
<div class="col" *ngIf="showRiskQ">
  <label>End Date<span style="color:red;font-size:x-small"> (*End Date Can't be less than start)</span></label>
  <input type="datetime-local" [(ngModel)]="downTimeToDate" placeholder="" [min]="minEndDate" />
</div>

Above my html and below my ts
  datetimefunction() {
    this.showRiskQ = true;
    this.updateEndDateMin();
  }

  updateEndDateMin() {
    const fromDate = new Date(this.downTimeFromDate);
    fromDate.setDate(fromDate.getDate() + 1);
    this.minEndDate = fromDate.toISOString().slice(0, 16);
  }
