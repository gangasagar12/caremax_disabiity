# CareMax Disability Staff Portal

## Staff Member Role & Access Control

This project implements a secure Staff Portal for CareMax Disability. Access to the portal is strictly controlled using Django's Group and Permissions system to ensure participant data privacy and system security.

### 1. The "Staff Group"
All staff members must be assigned to the **"Staff Group"** via the Django Admin panel. 
The system uses a custom `StaffRequiredMixin` on the backend to ensure that *only* members of this specific group (or Superusers) can access the portal routes.

### 2. Strict Data Filtering (Assignments)
Staff members **cannot** view all records in the system. They can only view and interact with records that have been explicitly assigned to them by an Administrator.
- **Participants**: Staff can only view participants where they are listed in the `assigned_staff` field. Unassigned participants or participants assigned to other staff members are completely hidden from their view.
- **Referrals**: Staff can only view referrals where they are listed in the `assigned_staff` field.
- **Support Plans, Case Notes, Documents**: Staff can only view these records if they belong to a participant explicitly assigned to them.

### 3. Portal Navigation (Allowed Access)
The Staff Portal Sidebar is restricted to the following areas:
- **Dashboard**: Displays personal statistics and upcoming activities based *only* on the staff member's assigned participants and referrals. Global system statistics (like total company participants) are hidden.
- **Participants**: View assigned participants and their profiles (NDIS details, goals, support needs, emergency contacts).
- **Referrals**: Manage incoming referrals assigned to the staff member.
- **Support Plans**: Review and update progress on assigned support plans.
- **Case Notes**: Create new case notes and view/edit their own notes. Staff cannot edit notes created by other staff members.
- **Documents**: Upload and view documents related to assigned participants.
- **Leave Requests**: Create, view, and cancel their own personal leave requests.
- **Notifications**: View personal system alerts and updates.
- **My Profile**: Update personal contact information.

### 4. Restricted Actions (Denied Access)
For security and data integrity, Staff members are explicitly **restricted** from performing the following actions:
- ❌ Creating new Participants or Referrals (this is an Admin/Management function).
- ❌ Deleting Participants, Referrals, Support Plans, Case Notes, or Critical Documents.
- ❌ Approving or Rejecting Leave Requests.
- ❌ Accessing Employee Management, User/Group Management, or System Settings.
- ❌ Viewing Global Reports, Analytics, or Announcements Management.

### 5. Activity Logging
Every action taken by a staff member (such as creating a note or updating a plan) is recorded in the `ActivityLog` model for auditing purposes. Admin users can review these logs securely in the Django Admin panel.
