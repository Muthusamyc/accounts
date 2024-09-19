using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
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
                    NetworkCredential NetworkCred = new NetworkCredential
                    {
                        UserName = "noreply@microlabs.in",
                        Password = "Password@1"
                    };
                    smtpClient.Credentials = NetworkCred;

                    MailMessage mailMessage = new MailMessage
                    {
                        From = new MailAddress("noreply@microlabs.in"),
                        Subject = emailModel.Subject,
                        IsBodyHtml = true,
                        Body = emailModel.Body
                    };
                    
                    // Add To address
                    mailMessage.To.Add(emailModel.To);

                    // Add CC address only if it's not null or empty
                    if (!string.IsNullOrEmpty(emailModel.CC))
                    {
                        mailMessage.CC.Add(emailModel.CC);
                    }

                    ServicePointManager.SecurityProtocol = SecurityProtocolType.Tls | 
                                                           SecurityProtocolType.Tls11 | 
                                                           SecurityProtocolType.Tls12;
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
