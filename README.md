using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.ModelBinding.Binders;
using System.Net;
using System.Net.Mail;

namespace IT_Portal.API.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class EmailController : ControllerBase
    {
        [HttpPost]
        public IActionResult SendEmail(EmailModel emailModel)
        {
            try
            {
                using (SmtpClient smtpClient = new SmtpClient("smtp-relay.gmail.com", 25))
                {
                    // No credentials needed for SMTP without authentication
                    smtpClient.UseDefaultCredentials = false;
                    smtpClient.EnableSsl = false;
                    System.Net.NetworkCredential NetworkCred = new System.Net.NetworkCredential();
                    NetworkCred.UserName = "noreply@microlabs.in";
                    NetworkCred.Password = "Password@1";
                    smtpClient.Credentials = NetworkCred;
                    MailMessage mailMessage = new MailMessage();
                    mailMessage.From = new MailAddress("noreply@microlabs.in");
                    mailMessage.To.Add(emailModel.To);
                    mailMessage.CC.Add(emailModel.CC);

                    mailMessage.Subject = emailModel.Subject;
                    mailMessage.IsBodyHtml = true;
                    mailMessage.Body = emailModel.Body;
                    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls| SecurityProtocolType.Tls11 | SecurityProtocolType.Tls12;
                    smtpClient.Send(mailMessage);
                }
                return Ok("Email sent successfully");
            }
            catch (Exception ex)
            {
                return StatusCode(500, $"Failed to send email: {ex.Message}");
            }
        }
    }

    public class EmailModel
    {
        public string? To { get; set; }
        public string? CC { get; set; }
        public string? Subject { get; set; }
        public string? Body { get; set; }
    }
}
